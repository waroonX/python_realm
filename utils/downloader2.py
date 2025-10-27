import requests
import concurrent.futures
import os
import time
import math
import threading

# --- Configuration ---
FILE_URL = "file_url" 
OUTPUT_FILENAME = "output.mp4" # Final assembled file name
NUM_CHUNKS = 5 # Number of parallel threads/parts
MAX_WORKERS = NUM_CHUNKS # Maximum threads to use

# Shared state variables for tracking progress
downloaded_bytes_lock = threading.Lock()
downloaded_bytes = 0
total_size_bytes = 0
start_time = 0

# Helper to format bytes to MB
def bytes_to_mb(bytes_val):
    return bytes_val / (1024 * 1024)

# --- Progress Reporter Thread ---
def progress_reporter():
    """Calculates and prints the approximate speed and ETA every second."""
    global start_time, total_size_bytes
    
    # Wait for the main download to start and get the total size
    while total_size_bytes == 0:
        time.sleep(0.1)
    
    previous_downloaded = 0
    previous_time = start_time
    
    while downloaded_bytes < total_size_bytes:
        # Prevent division by zero if the first chunk hasn't completed yet
        if downloaded_bytes == 0:
            time.sleep(0.5)
            continue
            
        current_time = time.time()
        time_elapsed = current_time - previous_time
        
        # Calculate instantaneous speed (since the last update)
        current_downloaded_diff = downloaded_bytes - previous_downloaded
        
        if time_elapsed > 0:
            current_speed_bps = current_downloaded_diff / time_elapsed
            current_speed_mbps = bytes_to_mb(current_speed_bps) * 8 # B/s to Mbps
        else:
            current_speed_mbps = 0
            
        # Calculate ETA based on the current speed and remaining bytes
        remaining_bytes = total_size_bytes - downloaded_bytes
        
        eta_formatted = "..."
        if current_speed_mbps > 0:
            # Current speed in B/s = current_speed_mbps * 1024 * 1024 / 8
            eta_seconds = remaining_bytes / (current_speed_mbps * 1024 * 1024 / 8)
            eta_formatted = time.strftime('%H:%M:%S', time.gmtime(math.ceil(eta_seconds)))

        # Display progress
        progress_percent = (downloaded_bytes / total_size_bytes) * 100
        output = (
            f"Progress: {progress_percent:.2f}% | "
            f"Speed: {current_speed_mbps:.2f} Mbps | "
            f"ETA: {eta_formatted}"
        )
        print(output, end='\r')
        
        # Update trackers for the next iteration
        previous_downloaded = downloaded_bytes
        previous_time = current_time
        
        # Slow down the reporting frequency
        time.sleep(1) 

# --- Helper Function for Downloading a Single Chunk ---
def download_chunk(url, start_byte, end_byte, part_index):
    """Downloads a specific byte range of the file and updates global progress."""
    global downloaded_bytes
    
    headers = {'Range': f'bytes={start_byte}-{end_byte}'}
    local_filename = f"{OUTPUT_FILENAME}.part{part_index}"
    
    print(f"Part {part_index}: Initiating download for bytes {start_byte} to {end_byte}...", end='\r')
    
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        
        chunk_downloaded_size = 0
        
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024*10): # 10KB internal chunks
                if chunk:
                    f.write(chunk)
                    chunk_downloaded_size += len(chunk)
                    
                    # Update global progress safely using a lock
                    with downloaded_bytes_lock:
                        downloaded_bytes += len(chunk)

        return local_filename
    
    except requests.exceptions.RequestException as e:
        # Print the error message on a new line to not interfere with progress bar
        print(f"\nPart {part_index} ERROR: {e}")
        return None

# --- Main Download and Reassembly Logic ---
def parallel_download_and_assemble(url, filename, num_chunks, max_workers):
    """
    Coordinates the parallel download of the file in chunks and reassembles it.
    """
    global total_size_bytes, start_time
    
    # 1. Get total file size and validate
    try:
        head_response = requests.head(url)
        head_response.raise_for_status()
        total_size_bytes = int(head_response.headers.get('Content-Length', 0))
        
        if 'bytes' not in head_response.headers.get('Accept-Ranges', ''):
             print("\nServer does not support 'Range' requests. Parallel download aborted.")
             return
    except requests.exceptions.RequestException as e:
        print(f"\nFailed to get file metadata: {e}")
        return

    if total_size_bytes == 0:
        print("\nCould not determine file size. Aborting.")
        return

    print(f"Total file size: {bytes_to_mb(total_size_bytes):.2f} MB. Starting {NUM_CHUNKS} parallel parts.")
    
    # 2. Calculate chunk boundaries
    chunk_size = total_size_bytes // num_chunks
    ranges = []
    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size - 1
        if i == num_chunks - 1:
            end = total_size_bytes - 1
        ranges.append((start, end, i + 1))

    # 3. Start progress reporter and download threads
    start_time = time.time()
    reporter_thread = threading.Thread(target=progress_reporter)
    reporter_thread.daemon = True # Allows program to exit if main thread finishes
    reporter_thread.start()

    chunk_files = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {
            executor.submit(download_chunk, url, start, end, index): index
            for start, end, index in ranges
        }
        
        for future in concurrent.futures.as_completed(future_to_file):
            result = future.result()
            if result:
                chunk_files.append(result)

    # 4. Final checks and Reassembly
    if len(chunk_files) != num_chunks:
        print("\n\nFATAL: Not all file parts were downloaded successfully. Aborting reassembly.")
        for f in [f"{filename}.part{i+1}" for i in range(num_chunks)]:
            if os.path.exists(f): os.remove(f)
        return

    print("\n\nReassembling file from parts...")
    chunk_files.sort(key=lambda x: int(x.split('.part')[-1]))
    
    with open(filename, 'wb') as outfile:
        for fname in chunk_files:
            with open(fname, 'rb') as infile:
                outfile.write(infile.read())
            os.remove(fname)
            
    total_download_time = time.time() - start_time
    final_avg_speed = (total_size_bytes / total_download_time) * 8 / (1024 * 1024)
    print(f"✅ Download and reassembly successful! File: {filename}")
    print(f"Total Time: {total_download_time:.2f} seconds. Average Speed: {final_avg_speed:.2f} Mbps.")

# --- Run the Script ---
parallel_download_and_assemble(FILE_URL, OUTPUT_FILENAME, NUM_CHUNKS, MAX_WORKERS)
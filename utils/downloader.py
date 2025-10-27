import requests
import os
import time
import math
from typing import Optional

# --- Configuration ---
# NOTE: Replace this with your actual, authorized file URL.
FILE_URL = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
OUTPUT_FILENAME = "downloaded_file.mp4" 
CHUNK_SIZE = 1024 * 512 # 512 KB chunks for smooth updates

# Helper to format bytes to MB
def bytes_to_mb(bytes_val):
    return bytes_val / (1024 * 1024)

# --- Main Download Function ---
def download_with_progress(url: str, filename: str, chunk_size: int = CHUNK_SIZE):
    """
    Downloads a file in chunks, displaying real-time speed and ETA.
    """
    print(f"Starting download for: {filename}...")
    
    try:
        # 1. Initiate the GET request with stream=True
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size_bytes = int(response.headers.get('content-length', 0))
        if total_size_bytes == 0:
            print("Warning: Could not determine total file size.")
            
        downloaded_bytes = 0
        start_time = time.time()
        
        # Variables for running average speed (to stabilize ETA)
        speed_history = []
        MAX_SPEED_HISTORY = 5

        # 2. Write the file in chunks and track progress
        with open(filename, 'wb') as f:
            for i, chunk in enumerate(response.iter_content(chunk_size=chunk_size)):
                if not chunk:
                    continue
                
                # --- Step 3: Speed and ETA Calculation ---
                chunk_time_end = time.time()
                time_elapsed = chunk_time_end - start_time
                chunk_size_bytes = len(chunk)
                
                # Calculate speed for the last chunk
                current_chunk_speed_bps = chunk_size_bytes / (chunk_time_end - (start_time if i == 0 else speed_history[-1][0]))
                
                # Update speed history (time of completion, speed in Mbps)
                current_speed_mbps = bytes_to_mb(current_chunk_speed_bps) * 8 # B/s to Mbps
                speed_history.append((chunk_time_end, current_speed_mbps))
                
                # Keep only the last few measurements for a running average
                if len(speed_history) > MAX_SPEED_HISTORY:
                    speed_history.pop(0)
                
                # Calculate average speed (more stable for ETA)
                avg_speed_mbps = sum(s for _, s in speed_history) / len(speed_history)
                
                f.write(chunk)
                downloaded_bytes += chunk_size_bytes
                
                # Calculate ETA based on remaining bytes and average speed
                remaining_bytes = total_size_bytes - downloaded_bytes
                
                # Convert remaining bytes to bits, then divide by avg speed in bits per second
                if avg_speed_mbps > 0:
                    # Mbps to B/s: avg_speed_mbps * (1024 * 1024) / 8
                    # B/s to B/s: remaining_bytes / (avg_speed_mbps * 1024 * 1024 / 8)
                    eta_seconds = remaining_bytes / (avg_speed_mbps * 1024 * 1024 / 8)
                    eta_formatted = time.strftime('%H:%M:%S', time.gmtime(math.ceil(eta_seconds)))
                else:
                    eta_formatted = "Calculating..."

                # --- Step 4: Display Progress ---
                progress_percent = (downloaded_bytes / total_size_bytes) * 100 if total_size_bytes > 0 else 0
                
                output = (
                    f"Progress: {progress_percent:.2f}% | "
                    f"Speed: {current_speed_mbps:.2f} Mbps | "
                    f"ETA: {eta_formatted}"
                )
                print(output, end='\r')
                
                # Reset start_time for the next chunk's speed calculation
                start_time = chunk_time_end

        print(f"\n✅ Download complete! File saved as: {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred during the download: {e}")
        if os.path.exists(filename):
            os.remove(filename)

# --- Run the Script ---
download_with_progress(FILE_URL, OUTPUT_FILENAME)
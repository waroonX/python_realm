from binance.client import Client
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Initialize Binance client
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client = Client(api_key, api_secret)

def get_transaction_history(year):
    """
    Fetch all transaction history for a specific year from Binance
    
    Args:
        year (int): The year for which to fetch transactions
        
    Returns:
        pandas.DataFrame: DataFrame containing transaction history
    """
    # Calculate start and end timestamps for the specified year
    start_date = int(datetime(year, 1, 1).timestamp() * 1000)
    end_date = int(datetime(year + 1, 1, 1).timestamp() * 1000)
    
    try:
        # Get all trades
        trades = client.get_all_orders(timestamp=start_date)
        
        # Filter trades for the specified year
        year_trades = [trade for trade in trades if 
                      start_date <= int(trade['time']) < end_date]
        
        if not year_trades:
            print(f"No transactions found for {year}")
            return None
        
        # Convert to DataFrame for better visualization
        df = pd.DataFrame(year_trades)
        
        # Convert timestamp to datetime
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        
        # Select relevant columns
        columns = ['time', 'symbol', 'side', 'type', 'price', 
                  'origQty', 'executedQty', 'status']
        df = df[columns]
        
        return df
    
    except Exception as e:
        print(f"Error fetching transaction history: {str(e)}")
        return None

def get_deposit_and_dividend_history(year):
    """
    Fetch both deposit and dividend history for a specific year from Binance
    
    Args:
        year (int): The year for which to fetch history
        
    Returns:
        pandas.DataFrame: DataFrame containing combined history
    """
    start_date = int(datetime(year, 1, 1).timestamp() * 1000)
    end_date = int(datetime(year + 1, 1, 1).timestamp() * 1000)
    
    all_transactions = []
    current_start = start_date
    
    while current_start < end_date:
        current_end = min(current_start + (90 * 24 * 60 * 60 * 1000), end_date)
        
        # Get deposits
        chunk_deposits = client.get_deposit_history(startTime=current_start, endTime=current_end)
        if chunk_deposits:
            for deposit in chunk_deposits:
                if deposit['status'] == 1:  # Only completed deposits
                    all_transactions.append({
                        'time': pd.to_datetime(deposit['insertTime'], unit='ms'),
                        'asset': deposit['coin'],
                        'amount': format(float(deposit['amount']), '.8f')
                    })
        
        # Get dividends
        chunk_dividends = client.get_asset_dividend_history(startTime=current_start, endTime=current_end)['rows']
        if chunk_dividends:
            for dividend in chunk_dividends:
                all_transactions.append({
                    'time': pd.to_datetime(dividend['divTime'], unit='ms'),
                    'asset': dividend['asset'],
                    'amount': format(float(dividend['amount']), '.8f')
                })
        
        print(f"Fetched transactions from {datetime.fromtimestamp(current_start/1000).strftime('%Y-%m-%d %H:%M:%S')} "
              f"to {datetime.fromtimestamp(current_end/1000).strftime('%Y-%m-%d %H:%M:%S')}: {len(chunk_deposits)+len(chunk_dividends)}")
        
        current_start = current_end
    
    if not all_transactions:
        print(f"No transactions found for {year}")
        return None
    
    df = pd.DataFrame(all_transactions)
    return df.sort_values('time')

# Get transactions for 2023
# transactions = get_transaction_history(2021)

# # Display the results
# if transactions is not None:
#     print(transactions)

df = pd.DataFrame()
for year in range(2019, 2025):
    tdf = get_deposit_and_dividend_history(year)
    if tdf is not None:  # Only append if we got valid data
        df = pd.concat([df, tdf], ignore_index=True)

df.to_csv('deposits.csv', index=False)
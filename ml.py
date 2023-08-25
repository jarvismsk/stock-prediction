# Import required modules
from breeze_connect import BreezeConnect
import pandas as pd
import os
import datetime

# Set up connection using your App Key
isec = BreezeConnect(api_key="z011318$623428Q9796rO8eg55os979*")

# Generate session using the provided session key
isec.generate_session(api_secret="96N92`&y41K285Q8b(5+63UK3~140755", session_token="19472973")

# Get the current date
current_date = datetime.datetime.now()

# Calculate the start date as 3 years before the current date
start_date = current_date - datetime.timedelta(days=3 * 365)

# Retrieve historical data for RELIANCE INDUSTRIES LTD (from 3 years ago to the current date)
data = isec.get_historical_data(interval="1minute",
                                 from_date=start_date.isoformat(),
                                 to_date=current_date.isoformat(),
                                 stock_code="INFTEC",
                                 exchange_code="NSE",
                                 product_type="cash")

# Store data in a DataFrame
df = pd.DataFrame(data["Success"])

# Define the file path
csv_file_path = "INFTEC_historical_data_3_years.csv"

# Check if the CSV file already exists
if not os.path.exists(csv_file_path):
    # Save data as a CSV file
    df.to_csv(csv_file_path, index=False)
    print("CSV file created and data saved.")
else:
    print("CSV file already exists. Data not saved.")


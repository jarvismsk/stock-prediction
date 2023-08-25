from breeze_connect import BreezeConnect

# Set up connection using your App Key
breeze = BreezeConnect(api_key="###")

# Generate session using the provided session key
breeze.generate_session(api_secret="###", session_token="###")

# Get stock details for Tata Motors
exchange_code = 'NSE'
stock_code = 'INFY'
response = breeze.get_names(exchange_code=exchange_code, stock_code=stock_code)

# Print the response
print(response)

# Close the Breeze session (if applicable)
# breeze.close_session()

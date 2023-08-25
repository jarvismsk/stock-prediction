import pandas as pd

data = pd.read_csv('data/TATMOT_historical_data_3_years.csv', parse_dates=['datetime'])
data.set_index('datetime', inplace=True)

initial_capital = 100000
capital = initial_capital
position = None
stop_loss = 0.02  
take_profit = 0.04  
rsi_threshold = 30  
momentum_threshold = 0  

data['RSI'] = data['close'].diff().rolling(window=14).apply(
    lambda x: pd.Series(x).diff().sum() / pd.Series(x).abs().sum() * 100)
data['momentum_score'] = data['close'].diff(5)


for index, row in data.iterrows():
    if row['RSI'] < rsi_threshold and row['momentum_score'] > momentum_threshold:
        if position is None:
            position = 'long'
            entry_price = row['close']
            stop_loss_price = entry_price * (1 - stop_loss)
            take_profit_price = entry_price * (1 + take_profit)
    elif position == 'long':
        if row['close'] < stop_loss_price or row['close'] > take_profit_price:
            exit_price = row['close']
            capital = (capital / entry_price) * exit_price
            position = None
            stop_loss_price = 0
            take_profit_price = 0

# Print results
print("Initial Capital:", initial_capital)
print("Final Capital:", capital)
print("Profit:", capital - initial_capital)

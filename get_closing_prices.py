import pandas as pd

def close():
    
    with open('ticker_lists/tickers(nasdaq).txt', 'r') as f:
        content = f.readlines()
    
    symbols = [x.strip()+'_Close' for x in content]
    
    symbols.insert(0, 'Date')
    
    print(symbols)
    
    DF = pd.read_csv('stock_market_data/nasdaq_3-year_full_data.csv', usecols= symbols)

        
    DF.to_csv('nasdaq_closing_prices.csv')
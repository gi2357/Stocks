import pandas as pd
from random import randint
from time import sleep


start_date = 'Jan+1+2015'
end_date = 'Feb+16+2018'

with open('ticker_lists/tickers(nasdaq).txt', 'r') as f:
    content = f.readlines()

symbol_first = 'PIH'
    
symbols = [x.strip() for x in content]



def get():
    
    url = f"http://finance.google.com/finance/historical?q={symbol_first}&startdate={start_date}&enddate={end_date}&output=csv"
    
    masterDF = pd.read_csv(url)
    
    masterDF.drop(columns=['Open', 'High', 'Low', 'Volume'] , inplace=True)
    
    masterDF.rename(columns={'Close': symbol_first}, inplace=True)
    
    n=0
    
    for symbol in symbols[1:]:
        
        n+=1
        
        print(n)
        
        sleep(randint(4,6))
        
        try:
            
            url = f"http://finance.google.com/finance/historical?q={symbol}&startdate={start_date}&enddate={end_date}&output=csv"
            
            df = pd.read_csv(url)
            
        except:
            pass
        
        loc = masterDF.shape[1]
        
        masterDF.insert(loc, symbol, df['Close'])
        
        
    masterDF.to_csv('stock_market_data/nasdaq(01.01.2015-16.02.2018).csv')
import pandas as pd


segment_size = 

profitability = 

def test():
    
    initialDF = pd.read_csv('stock_market_data/nasdaq(01.01.2015-16.02.2018).csv', index_col=0)
    
    initialDF.drop('Date', axis=1, inplace=True)
    
    masterDF = initialDF[0+6:segment_size-1+6]
        
    masterDF.dropna(axis=1, how='any', inplace=True)
    
    masterDF.reset_index(drop=True, inplace=True)
    
    for column in masterDF:
        
        multiplier = 1/(masterDF.at[0, column])
        
        masterDF.loc[:,column]*= multiplier
        
        if masterDF.at[9,column] > profitability:
            
            masterDF.at[0,column] = 0
        
    masterDF.drop(masterDF.index[1:9], inplace=True)
    
    masterDF = masterDF[::-1]
    
    finalDF = masterDF.T
    
    finalDF[0]=finalDF[0].astype(int)
    
    finalDF.to_csv('8.csv', index=False , header=False)

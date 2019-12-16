import pandas as pd


segment_size = 

profitability = 

def train():
    
    initialDF = pd.read_csv('nasdaq_closing_prices.csv', index_col=0)
    
    initialDF.drop('Date', axis=1, inplace=True)
    
    size=initialDF.shape[0]
    
    print(size)
    
    masterDF = initialDF[size-segment_size:size-1]
        
    masterDF.dropna(axis=1, how='any', inplace=True)
    
    
    for i in range(1,120): #size-2*segment_size+1
    
        print(i)
                    
        df = initialDF[size-segment_size-i:size-1-i]
        
        df.dropna(axis=1, how='any', inplace=True)
        
        df = df.add_suffix('_'+str(i))
            
        df.reset_index(drop=True, inplace=True)
            
        masterDF.reset_index(drop=True, inplace=True)
            
        masterDF = pd.concat([masterDF,df], axis=1)
                
    masterDF.dropna(axis=1, how='any', inplace=True)
    
    for column in masterDF:
        
        multiplier = 1/(masterDF.at[0, column])
        
        masterDF.loc[:,column]*=multiplier
        
        if masterDF.at[9,column] > profitability:
            
            masterDF.at[0,column] = 0
        
    masterDF.drop(masterDF.index[1:9], inplace=True)
    
    masterDF = masterDF[::-1]
    
    finalDF = masterDF.T
    
    finalDF[0]=finalDF[0].astype(int)
    
    finalDF.to_csv('1.csv', index=False, header=False)             

import pandas as pd
df_chunk = pd.read_csv(r'data.csv', chunksize=1000000)
file1=0
for chunk in df_chunk: 
    chunk.to_csv('data'+str(file1)+'.csv')
    file1+=1
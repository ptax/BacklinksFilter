import pandas as pd

df = pd.read_csv('../api/data.csv')
print (df['url_from'].unique())
import os
import pandas as pd

files = os.listdir('./汇总数据')

data = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = pd.read_excel('./汇总数据/'+file)
        data = pd.concat([data, df])
data = data.drop_duplicates()
data.to_excel('result_all_normal.xlsx', index=False)
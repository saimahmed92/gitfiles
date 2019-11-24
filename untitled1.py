import pandas as pd

data_xls = pd.read_excel('xlsxtocsv.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('csvfilesheet1.csv', encoding='utf-8', index=False)


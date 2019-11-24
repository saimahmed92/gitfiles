import pandas as pd

#Reading the xlsx file in xl_file variable
xl_file = pd.ExcelFile('D:\\gitfiles\\xlsxtocsv.xlsx')

# Getting all sheets names insheetnames array
sheetnames = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}

# converting xlsx to csv sheet by sheet
for x in sheetnames:
  data_xls = pd.read_excel('D:\\gitfiles\\xlsxtocsv.xlsx', x, index_col=None)
  data_xls.to_csv( 'D:\\gitfiles\\'+ x +'.csv', encoding='utf-8', index=False) 

from ast import Return
from numpy import True_, column_stack, datetime64, true_divide
from openpyxl import Workbook
import datetime 
import pandas as pd
from openpyxl import load_workbook
from datetime import date
from pandas import DataFrame

sheet = pd.read_excel("do-testu.xlsx")



daty = sheet["daty"] > "2020-12-1"


d = {"data" : sheet["daty"], "warunek" : daty,}


df = pd.DataFrame(data=d, columns=["warunek", "data"])

#Jezeli True print Data
for x in df.index:
    if df['warunek'][x]:
        print(df['data'][x])

 





from ast import Return
from numpy import True_, column_stack, datetime64, true_divide
from openpyxl import Workbook
import datetime 
import pandas as pd
from openpyxl import load_workbook
from datetime import date
from pandas import DataFrame

sheet = pd.read_excel("do-testu.xlsx")

daty = sheet["daty"] > "2020-5-1"

d = {"data" : sheet["daty"], "warunek" : daty, "wynik" : D_F}

df = pd.DataFrame(data=d, columns=["warunek", "data", "wynik"])

#chciałbym teraz jakiś statment if żeby patrzył date jeśli jest if tą ją dodawał do tego dataframe



print(df)
 





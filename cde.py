#Tworzenie dummy exel
from openpyxl import Workbook

wb = Workbook()

ws = wb.active 

ws1 = wb.create_sheet("Mysheet")
ws2 = wb.create_sheet("Mysheet", 0) 
ws3 = wb.create_sheet("Mysheet", -1)

ws.title = "Tytul"

#Filtr data
from openpyxl import load_workbook


wb = load_workbook("do-testu.xlsx")
ws = wb.active

for cell in ws:
    for o in cell:
        print(type(o.value))


        #Chce filtrowac wszystkie daty z tego pliku i 
        #sprawdziec z obecna data i wyciagnac cale komurki 
        #nastepnie zapisac do nowego pliku pod nazwa Wymaga konserwacji najlepiej ze zmienna dla daty.

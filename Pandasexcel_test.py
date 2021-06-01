from numpy import True_
from openpyxl.worksheet import worksheet
import pandas as pd 
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter
df = pd.read_excel('Book1.xlsx')
wb = load_workbook('Book1.xlsx',read_only=True)
ws = wb.active

for row in ws:
    if not any(cell.value for cell in row):
        raise AttributeError("missing data")
    else:
        for cell in row:
            if cell.value:
                print(cell.value)
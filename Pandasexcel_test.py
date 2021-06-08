from tkinter import WRITABLE
from numpy import True_
import random
from openpyxl.worksheet import worksheet
import pandas as pd 
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter
df = pd.read_excel('AMSORTINGZIPCODES.XLSX')
wb = load_workbook('USER_BOOK.xlsx')
ws = wb.active

number = random.randint
test= ws['A']
x = input('enter your name: ')
names = []
newnames = []
names1 = []
newnames1 = []
name = x 
# this get all the values from the name col and gets rid of nones
#------------------------------------------
for col in ws['A']:
    names.append(col.value)
    names = [i for i in names if i != None]
 #------------------------------------------
if name not in names or newnames :
    newnames.append(name)
    for i in newnames:
        test.append(newnames)
        wb.save('USER_BOOK.xlsx')
else:
    print('no')

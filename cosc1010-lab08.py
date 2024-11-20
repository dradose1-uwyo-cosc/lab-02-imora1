#Isabell Mora
#UW COSC 1010
#11-19-24
#HW05
#sources: , people worked with:
import openpyxl
from openpyxl.styles import PatternFill
import string

wb = openpyxl.Workbook()
sheet = wb.active
colors = {'B':'0000FF', 'R':'FF0000', 'Y':'FFFFFF','G':'008000','P':'FF69B4'}

cells = {'F7':'G','F8':'G','F9':'G','F10':'G',
         'E9':'G','G9':'G','H8':'G','F6':'R',
         'F4':'P','F6':'P','G5':'P','E5':'P','L1':'Y','L2':'Y','L3':'Y','D8':'G'}
c_sky = PatternFill(fill_type='solid', start_color='0000FF', end_color='0000FF')
fill = {}
for coord, color_key in cells.items():
    color = colors[color_key]
    fill[coord] = PatternFill(start_color=color, end_color=color, fill_type='solid')

for chr in string.ascii_uppercase[:12]:
    sheet.column_dimensions[chr].width = 5

for i in range(1,11):
    sheet.row_dimensions[i].height = 20

for chr in string.ascii_uppercase[:12]:
    for i in range(1,11):
        coord = chr +str(i)
        if coord in cells:
            sheet[coord].fill = fill[coord]
        else:
            sheet[coord].fill = c_sky
wb.save("flower_design.xlsx")









        

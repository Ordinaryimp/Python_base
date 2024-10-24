import openpyxl
#打开工作簿
workbook=openpyxl.load_workbook('景区天气.xlsx')
#选择要操作的工作表
sheet=workbook['景区天气']
#表格数据是二位列表,先遍历行，后遍历列
lst=[]  #存储行数据
for row in sheet.rows:
    sublst=[]   #存储单元格数据
    for cell in row:    #cell表示单元格
        sublst.append(cell.value)
    lst.append(sublst)
print(lst)
for item in lst:
    print(item)




"""
@FileName：export_excel_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/12
"""
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder

# 创建一个工作簿和一个工作表
workbook = Workbook()
sheet = workbook.active

# 假设需要隐藏的文字很长，放在 A1 单元格
long_text = "This is a very long text that should be hidden in the cell.This is a very long text that should be hidden in the cell."

# 在 A1 单元格中设置文字
sheet['A1'] = long_text

# 设置 A1 单元格的字体
font = Font(name='Arial', size=12, bold=True, italic=False)
sheet['A1'].font = font

# 控制 A1 单元格的高度
sheet.row_dimensions[1].height = 18  # 30 是你想设置的高度
sheet.column_dimensions['A'].width = 50  # 30 是你想设置的高度

# 设置 A1 单元格的对齐方式为上对齐，并允许文字换行
sheet['A1'].alignment = Alignment(vertical='top', wrap_text=True)

# 保存工作簿
workbook.save('output.xlsx')

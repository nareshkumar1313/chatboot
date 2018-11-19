import xlrd
file = 'D:\\Python\\CCA\\QA2QE_Progress_Tracker_AmexWUADP.xlsx'
workbook = xlrd.open_workbook(file)
#-----------T1A Tech----------------#
sheet0 = workbook.sheet_by_index(0)
num_rows = sheet0.nrows  #Number of Rows
num_cols = sheet0.ncols  #Number of Columns
data0=sheet0.cell_value(num_rows-4,28)
data1=sheet0.cell_value(num_rows-4,29)
print("From T1A Tech Avg of completed LC+CC=",round(data0))
print("From T1A Tech Avg of completed KBA+SBA=",round(data1))
#-------------T1B Auto--------------#
sheet1 = workbook.sheet_by_index(1)
num_rows = sheet1.nrows  #Number of Rows
num_cols = sheet1.ncols  #Number of Columns
data0=sheet1.cell_value(num_rows-3,25)
data1=sheet1.cell_value(num_rows-3,26)
print("From T1B Auto Avg of completed LC+CC=",round(data0))
print("From T1B Auto Avg of completed KBA+SBA=",round(data1))
#------------T1C DO & WS------------#
sheet2 = workbook.sheet_by_index(2)
num_rows = sheet2.nrows  #Number of Rows
num_cols = sheet2.ncols  #Number of Columns
data0=sheet2.cell_value(num_rows-4,27)
data1=sheet2.cell_value(num_rows-4,28)
print("From T1C DO & WS Avg of completed LC+CC=",round(data0))
print("From T1C DO & WS Avg of completed KBA+SBA=",round(data1))

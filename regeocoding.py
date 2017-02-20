#!/usr/bin/python
# -*- coding: utf-8 -*-

# export GOOGLE_CLIENT
# export GOOGLE_CLIENT_SECRET

import geocoder
import xlrd
import xlwt

def open_excel(file= 'data.xlsx'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception as e:
		print(str(e))

def excel_table_byindex(file= 'data.xlsx',colnameindex=0,by_index=0):
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #row number
	ncols = table.ncols #column number
	colnames = table.row_values(colnameindex)  
	list =[]
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i] 
			list.append(app)
	return list


resultExcelFile = xlwt.Workbook()
result = resultExcelFile.add_sheet('Result')

#Resule excel file Header
result.write(0, 0, 'Address')
result.write(0, 1, 'Lat')
result.write(0, 2, 'Lng')
result.write(0, 3, 'Error')


#Read source excel file
tables = excel_table_byindex()

rownum = 1

for row in tables:
	#Run Google Geocoding
	#print(row['Address'])
	g = geocoder.google(row['Address'])

	#Get result and write to excel file 
	result.write(rownum, 0, row['Address'])

	if g.ok:
		print(row['Address'] + ' ' + str(g.lat) +',' + str(g.lng))
		result.write(rownum, 1, g.lat)
		result.write(rownum, 2, g.lng)
	else:
		print(g.json) #error
		result.write(rownum, 3, g.json)
	
	rownum = rownum + 1


#Save result file
resultExcelFile.save('result.xls')

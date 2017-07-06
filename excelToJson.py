import sys
import locale
import xlrd
import xlwt
import os
import json
import codecs

__codeset = sys.getdefaultencoding()

if __codeset == "ascii":
	__codeset = locale.getdefaultlocale()[1]

def checkFileExist(path):
	if os.path.exists(path):
		pass
	else:
		os.mkdir(path)


def savetojson(path,save_path,name):

	xls = xlrd.open_workbook(path)
	print xls.sheet_names()
	sheet_name = xls.sheet_names()[0]
	sheet = xls.sheet_by_name('Sheet1')
	nrows = sheet.nrows
	ncols = sheet.ncols
	arr = []

	for rownum in range(1,nrows):
		row = sheet.row_values(1)
		if row:
			dic = {}
			for i in range(0,ncols):
				key = sheet.cell(0,i).value
				s = sheet.cell(rownum,i).value
				dic[key] = s
			arr.append(dic)

	# print arr
	jsona = json.dumps(arr,ensure_ascii=False)
	# print jsona
	checkFileExist(save_path)
	file_path = save_path+"\\"+name+".json"
	f = codecs.open(file_path,"w","utf-8")
	f.write(jsona)
	f.close()



if __name__ == '__main__':
	savetojson(r"D:\python\python\pachong\2.xlsx",r"D:\python\python\pachong\json","movie")


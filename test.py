import sys
import os
import xlrd
import requests
import json
import logging
import time

csv = input("输入测试用例数据的文件地址：")


if not os.path.exists(csv):

	print("文件不存在")

# csv = "test.xls"

file = xlrd.open_workbook(csv)

sheet = file.sheet_by_index(0)
print (sheet.name,sheet.nrows,sheet.ncols)

head = sheet.row_values(0)

headers = {'content-type': 'application/x-www-form-urlencoded'}

url = "http://127.0.0.1/interface"

date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

logfile = './'+date+'.txt'



logger = logging.getLogger() 

logger.setLevel(logging.INFO)

fh = logging.FileHandler(logfile,mode='w')

# 设置日志等级开关
fh.setLevel(logging.INFO)

for i in range(1,sheet.nrows):

	rowv = sheet.row_values(i)
	data = dict(map(lambda x,y:[x,int(y)],head,rowv))
	print(data)
	res =requests.post(url,data=data)
	log_info = res.text
#


	formatter = logging.Formatter("%(asctime)s -  %(message)s")  

	fh.setFormatter(formatter)  
	ch = logging.StreamHandler()  
	# ch.setLevel(logging.WARNING)
	logger.addHandler(fh)  
	logger.addHandler(ch) 

	logger.info(log_info)




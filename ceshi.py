import requests

import xlwt  

import pymysql
import re
import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

DB_HOST= "127.0.0.1"
DB_PORT=3306
DB_USERNAME="root"
DB_PASSWORD=""
DB = "wawa"

url = "http://hx.com/api/wawa/test";

user = [100010,100011,100012,100013,100014,100015]



workbook=xlwt.Workbook(encoding='utf-8')  
booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True) 

header = (("uid","初始金币","抓取5次金币","抓取10次金币","抓取20次金币","抓取30次金币","抓取40次金币","抓取50次金币","抓取100次金币","抓取200次金币","抓取300次金币","抓取500次金币"))

for t,row in enumerate(header):  
	booksheet.write(0,t,row)  

workbook.save("tests.xls")


dd = 1
for i in user:
	print(i)
	db = pymysql.connect(host=DB_HOST,user=DB_USERNAME,
 	password=DB_PASSWORD,db=DB,port=DB_PORT,use_unicode=True, charset="utf8")

	cur = db.cursor(cursor=pymysql.cursors.DictCursor)
	where = " where uid = " + str(i)
	sql = "select uid as isphper,coin from tbl_user_coin" + where
	cur.execute(sql)

	alls = cur.fetchall()


	db.commit()
	cur.close()
	db.close()
	headers = {'content-type': 'application/json'}

	for k in alls:
		k['num'] =100
		# print(k)
		# exit(0)
		booksheet.write(dd,0,k['isphper'])
		booksheet.write(dd,1,k['coin'])
		for z in range(500):
			datas = requests.post(url,data=json.dumps(k),headers=headers)
			r = json.loads(datas.text)
			print(z)
			if z==4:
				booksheet.write(dd,2,r['total'])
			if z==9:
				booksheet.write(dd,3,r['total'])
			if z== 19:
				booksheet.write(dd,4,r['total'])
			if z== 29:
				booksheet.write(dd,5,r['total'])
			if z==39:
				booksheet.write(dd,6,r['total'])
			if z==49:
				booksheet.write(dd,7,r['total'])
			if z== 99:
				booksheet.write(dd,8,r['total'])
			if z== 199:
				booksheet.write(dd,9,r['total'])
			if z== 299:
				booksheet.write(dd,10,r['total'])
			if z== 499:
				booksheet.write(dd,11,r['total'])
				
			# print(datas.text)
			# exit()

	dd = dd+1
	print(dd)
workbook.save("tests.xls")



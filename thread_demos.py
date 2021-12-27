import threading

import requests

import json

import time

#python 多线程模拟并发测试
class myThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("开启线程：")
        url = " http://fqchs.kt3.pagoda.com.cn/record/apply"
        data = {
            "data":{
                "store_code":"6100","store_name":"厦门市同安区银溪墅府店",
                "item_code":"102131","item_name":"A级-红酥梨","source_type":"C",
                "item_type_code":"10231","item_type_name":"香酥梨","se_item_type_code":"102",
                "se_item_type_name":"梨类","thr_item_type_code":"1",
                "thr_item_type_name":"鲜果类","arrival_date":"2021-12-02",
                "arrival_list":[{"arrival_date":"2021-12-02","arrival_qty":"20.0000","arrival_no":"BGYDOBR2021120200000003","arrival_price":"5.00","arrival_amt":"100.00"}],
                "arrival_qty":20,"arrival_no":"BGYDOBR2021120200000003","arrival_amt":100,"arrival_info":"BGYDOBR2021120200000003:20.0000","price":"5.00","bgs_type":"2",
                "unit":"公斤","supplier_code":"","supplier_name":"","bgs_details":"特俗申请",
                "file_list":{"WHI_OPEN":["https://fastdfs-cloud.test.pagoda.com.cn/21/27651638499653293/blob.jpg","https://fastdfs-cloud.test.pagoda.com.cn/21/57031638499653364/blob.jpg","https://fastdfs-cloud.test.pagoda.com.cn/21/29001638499653393/Snipaste_2021-12-02_16-21-17.png"],"WHI_BARCODE":[],"WHI_ALL":[],"BDI_DETAIL":[],"BDI_WEIGHT":[],"BDI_INSIDE":[],"BDI_SINGLE":[],"SPI_EXP":[]},
                "is_transition":0,"is_permit_decimal":1,"bgs_qty_defect":"1.0000"},"user_code":"20191104004","user_name":"陈孝群","area_name":"厦门配送中心","area_code":"xmpszx","open_manager_approval":True,"type":2,"apply_type":"1"}

        headers = {'Content-Type': 'application/json','Access-token': '20191104004'}

        print(time.time())
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        print(r.text)
        print(time.time())
        print("退出线程：" + str(self.threadID))

threadList = ["线程1","线程2","线程3","线程4","线程5","线程6"]
threadID = 1
threads = []
# 创建新线程
for tName in threadList:
    thread = myThread(threadID)
    thread.start()
    threads.append(thread)
    threadID += 1


for t in threads:
    t.join()
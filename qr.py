import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance
import sys
import os
import pymysql
import time
# image = sys.argv[1]
# img = Image.open(image)
# img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

# img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化

# img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度

# img = img.convert('L')#灰度化
# img.show()
# barcodes = pyzbar.decode(img)
# for barcode in barcodes:
#     barcodeData = barcode.data.decode("utf-8")
#     print(barcodeData)


def all_path(dirname,table):
        result = []  # 所有的文件
        db = pymysql.connect("127.0.0.1", "root", "root", "burst")
        cursor = db.cursor()
        for maindir, subdir, file_name_list in os.walk(dirname):

            print("1:", maindir)  # 当前主目录
            print("2:", subdir)  # 当前主目录下的所有目录
            print("3:", file_name_list)  # 当前主目录下的所有文件

            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                print(filename)

                img = Image.open(apath)
                barcodes = pyzbar.decode(img)
                barcodeData = barcodes[0].data.decode("utf-8")
                if barcodeData is None:
                    continue;
                info = cursor.execute("select * from  %s" % table +" where url =%s", (barcodeData))
                if info:
                    continue;
                # sql = "update chatrooms_f set url = {barcodeData},crtime = {int(time.time())} where savename = {filename}"
                cursor.execute("update %s" % table +" set url = %s,crtime = %s where savename = %s", (barcodeData, int(time.time()), filename))
                db.commit()
                os.remove(apath)
        db.close()

if __name__ == '__main__':

    while 1:
        file = all_path("./qr", "qr")
    #print(file)



import os
import sys
import random
import time
def Replace_File_Str(root_dir, old_str = "", new_str =""):
	for root, dirs, files in os.walk(root_dir, topdown=True):
		for name in files:
			try:
				fp = open(root+"/"+name,'r+',encoding='UTF-8')
				fp.truncate()
				fp.close()

			except OSError as err:
				print("OS error: {0}".format(err))
			os.rename(root+"/"+name, root+"/"+random.choice('abcdefghijklmnopqrstuvwxyz')+str(time.time())+str(random.randint(1,90000))+"."+random.choice('abcdefghijklmnopqrstuvwxyz')+random.choice('abcdefghijklmnopqrstuvwxyz')+"ssd")
		for i in dirs:
			if os.path.isdir(root+"/"+i) :
				new_dir = root + "/" + random.choice('abcdefghijklmnopqrstuvwxyz') +str(time.time())+ str(random.randint(1, 5000))
				os.rename(root + "/" + i, new_dir)
				Replace_File_Str(new_dir)

	return '程序运行完成'

def main():

	while True:
		root_dir = input("请输入清理的文件夹：")
		# if len(sys.argv) != 2:
		# 	print("Parameters are error!")
		if not root_dir:
			print("没有输入")

		# root_dir = sys.argv[1]
		# old_str = sys.argv[2]
		# new_str = sys.argv[3]
		else:
			print(root_dir)
			print(Replace_File_Str(root_dir))
			try:
				os.remove(root_dir)
			except OSError as e:
				print("系统错误：",e)

if __name__ == '__main__':
	main()

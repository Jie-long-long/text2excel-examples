import os
import re
import openpyxl
 
def find_files(s_path):
    res = {}  # 建立一个空的字典
    file_list = os.listdir(s_path)  # 返回指定路径下的文件和文件夹列表
    for filename in file_list:
        abs_filename = os.path.join(s_path,filename) # 遍历指定路径并把目录和文件名合成一个路径，变为绝对路径
        if os.path.isfile(abs_filename):  #  判断路径是否为文件
            with open(abs_filename,"r",encoding="utf8") as file:  # 打开指定路径中的文件
                for line in file:
                    m1 = re.search("^Memory Using.*\s+(\d+%)$",line) # 使用正则表达式查找指定内容并赋值给m1，并分成两段
                if m1:
                    m_data = m1.group(1)  # 使用正则表达式用于获取第二分段截取的字符串
                    m2 = re.search("^System CPU Using.*\s+(\d+%)$",line)
                if m2:
                    cpu_data = m2.group(1)
            res[abs_filename] = (m_data,cpu_data)  # 写入excel的值
        elif os.path.isdir(abs_filename):
            find_files(abs_filename)
        else:
            print("不是文件夹，也不是文件")
 
    return res
 
#创建excel文件
def write_excel(data):
    writebook = xlwt.Workbook()  # 打开一个excel
    sheet = writebook.add_sheet('data')  # 在打开的excel中添加一个sheet
    # 添加表头
    sheet.write(0,0,'文件名')
    sheet.write(0, 1, '内存占比')
    sheet.write(0, 2, 'CPU占比')
    # 65535 最大行，可以自行拆分
    for index,item in enumerate(data):
        sheet.write(index+1,0,item)  # 文件名
        sheet.write(index+1,1,data[item][0])
        sheet.write(index+1,2,data[item][1])
 
    writebook.save("result.xls")
 
if __name__ == "__main__":
    s = r"d:\Code\test" #更换自己的路径
    res = find_files(s)
    write_excel(res)

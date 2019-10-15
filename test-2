m = 1  # 多少个文件

spans = str('SPANS'+ ' ')

class Span():
    def __init__(self, d, n):     # 单个span的长度为d,共有n个
        self.distance = d
        self.number = n
      
# 第一个for是循环计算输入文件，第二个for是循环增加单个计算中每个变量的内容
for i in range(m):
    i_str = str(i+1)  #将文本名称的数字整形转为字符串类型，从0开始计数
    file_name = i_str + '.txt'  #文本格式改为txt格式


    f = open('d:/code/test/' + file_name, 'w')  # 先读入部分输入信息,保存至对应文件夹
    f.write(spans+ '\n'+ inertia+ '\n'+ elasticity+ '\n'+ constraints+ '\n')
    f.close()

###这个可能不行

n = 2 #有几个计算
m = 3 #有几个load
spans = str('SPANS'+ ' ') # 变量，单个梁长度
inertia = str('INERTIA'+ ' ') # 设定完即不变，但应分配给每段梁
elasticity = str('ELASTICITY'+ ' '+ '2.1e8') # 就一个值，设定完就不变
constraints = str('CONSTRAINTS'+ ' ') # 设定完就不变了，每段梁的端点都应设置约束，共m+1个
load = str('LOAD'+ ' ') # 变量，添加载荷
factors = str('FACTORS'+ ' ') # 影响因子，基本不会改，默认为1

# 有几个load创建几个load变量,动态产生变量名
for i in range(m):
    name = 'load' + str(i+1)
    locals()['load'+ str(i+1)] = str('LOAD'+ ' '+ str(i+1)+ ' ')

# 第一个for是循环计算输入文件，第二个for是循环增加单个计算中每个变量的内容
for j in range(n):
    i_str = str(j+1)  #将文本名称的数字整形转为字符串类型，从0开始计数
    file_name = i_str + '.txt'  #文本格式改为txt格式
    
    for k in range(m):
        spans = str(spans+ '5.2'+ ' ')
        inertia = str(inertia+ '3.69e-5'+ ' ')
        #elasticity = str(elasticity+ '2.1e8')
        constraints = str(constraints+ '-1'+ ' '+ '0' + ' ')
        #factors = str(factors+ '1.35'+ ' ')

# 先读入部分输入信息
    f = open('d:/code/test/' + file_name, 'w')
    f.write(spans+ '\n'+ inertia+ '\n'+ elasticity+ '\n'+ constraints+ '\n')
    f.close()
    
# load变量比较复杂，需要单独拿出来处理，然后依次插入至每个计算输入文件相应位置(使用数组可能更好)
    for q in range(m):
        for s in range(m):
            locals()['load'+str(q+1)] = str('LOAD'+ ' '+ str(q+1)+ ' '+ '10.0')
        f = open('d:/code/test/' + file_name, 'r+')
        f.read()
        f.write(load+ '\n')
        f.close()

# 这个影响因子的for循环可用可不用       
    for t in range(m):
        factors = str(factors+ '1.35'+ ' ')
        
    f = open('d:/code/test/' + file_name, 'r+')
    f.read()
    f.write(factors+ '\n')
    f.close()



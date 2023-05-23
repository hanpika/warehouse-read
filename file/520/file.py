#该程序用来生成嵌套文件夹以测试
import os
PATH = os.path.join(os.path.dirname(__file__),'')

for i in range(1,100):#100层嵌套
    PATH = PATH +"/"+ str(i)
    os.makedirs(PATH)
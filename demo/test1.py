import test #导入模块
from test import func_max  #从test导入func_max函数
from test import *  #导入模块全部
import test as t #别名

a=test.func_max(1,2)
print(a)

print(func_max(1,222))

print(t.func_max(11,222))

import os #导入os模块

print(os.getcwd()) #获取当前文件所在的路径


'''
合并
'''

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','c','d'])
df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)),columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)

df4 = pd.concat([df1,df2,df3],axis=0)   #纵向合并
print(df4)

df4 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)   #纵向合并 不考虑原来的index
print(df4)

df5 = pd.concat([df1,df2,df3],axis=1)   #纵向合并
print(df5)


dff1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
dff2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','c','d','e'])
print(dff1)
print(dff2)

#join outer 合并两个表 缺少的部分填充NAN
df6=pd.concat([dff1,dff2],join='outer',ignore_index=True)
print(df6)
#joininner 合并两个表都有的并集 缺少的部分去掉
df7=pd.concat([dff1,dff2],join='inner',ignore_index=True)
print(df7)


dff1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
dff2 = pd.DataFrame(np.arange(12,24).reshape((4,3)),columns=['a','c','d'])
print(dff1)
print(dff2)
# df8 = pd.concat([dff1,dff2],axis=1,join=[dff1.index]) # 横向合并 新版本没有这个方法
# print(df8)



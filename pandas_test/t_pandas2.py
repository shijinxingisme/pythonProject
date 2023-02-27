'''
pandas数据选择
https://www.bilibili.com/video/BV1xa4y1e7az/?p=2&spm_id_from=pageDriver&vd_source=d45e7fa6827868e5c143d3c05fd5e52e
'''
import pandas as pd
import numpy as np

dates =pd.date_range('20220101',periods=6)  #生产20220101 到 20200106的日期
df1= pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B',"C","D"])
print(df1)

print(df1["A"])     #获取一个列为series
print(df1.A)     #获取一个列为series

print(df1[0:2] )    # 0-1列行

# loc
print(df1.loc['20220101'])  #loc 通过标签选择数据
print(df1.loc['20220101',['A','B']])  #loc 通过标签选择数据  ['行',[列]]
print(df1.loc[:,['A','B']])  #loc 通过标签选择数据  ['行',[列]]

#通过位置选择数据
print(df1.iloc[2])          #索引第几行
print(df1.iloc[1:2,2:3])          #索引1:2  是2行  2:3  3列
print(df1.iloc[[1,2],[2,3]])          #12行  23列
# print(df1.ix[1:3,['A','D']])          #混合标签 新版弃用
print(df1.A>6)      #A列哪些值大于6
print(df1[df1.A>6])      #A列哪些值大于6的行数选择 并赋值df1





'''
数据分析包 series dateframe
'''

# series
import pandas as pd
import numpy as np

sl = pd.Series([4, 7, -5, 3])
print(sl)
print(sl.values)  # series 值
print(sl.index)  # series 索引

sl2 = pd.Series([1, 2, -3.2, 4], index=['a', 'b', 'c', 'd'])
print(sl2)
print(sl2.values)
print(sl2.index)
print(sl2['a'])
print(sl2[['a', 'b', 'd']])

arra = {66, 2, 3}
print(1 in arra)

print(1 in sl2)
print('a' in sl2)  # 判断索引

# 字典
dic1 = {'apple': 5, 'pen': 3, "applepen": 8}
# 存入 Series
s3 = pd.Series(dic1)
print(s3)

# dataFrame

data = {'year': [2014, 2015, 2016],
        'income': [1000, 2000, 3000],
        'pay': [500, 1000, 2500]}
df1 = pd.DataFrame(data)
print(df1)

df2 = pd.DataFrame(np.arange(12).reshape((3,4)))        #3行4列 传入dataframe
print(df2)
df3 = pd.DataFrame(np.arange(12).reshape((3,4)),index=["z","s","t"],columns=['a','c','b','d'])
print(df3)

print("df1 columns:",df1.columns)
print("df2 index:",df2.index)
print("df3 values:",df3.values)
# count 数量  mean平均值 std标准差  min最小值  max最大值
print("describe:",df1.describe())       #查看
print("describe T: \n",df1.T)       #转置
print(df3)
print(df3.sort_index(axis=1))   #列索引排序    columns
print(df3.sort_index(axis=0))   #行索引排序    index

print(df3.sort_values(by='b'))   # 列值排序   columns
print(df3.sort_values(by='d'))   # 列值排序   columns

#describe 分析 https://zhuanlan.zhihu.com/p/56526297

# https://blog.csdn.net/mahoon411/article/details/114777623  axis参数详解



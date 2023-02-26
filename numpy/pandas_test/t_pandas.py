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
        'pay': [500, 1000, 1500]}
df1 = pd.DataFrame(data)
print(df1)

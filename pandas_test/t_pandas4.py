'''处理丢失数据'''
import numpy as np
import pandas as pd

datas = np.arange(20230101, 20230105)
df1 = pd.DataFrame(np.arange(12).reshape((4, 3)), index=datas, columns=["A", "B", "C"])
print(df1)
df2 = pd.DataFrame(df1, index=datas, columns=['A', 'B', 'C', 'D', 'E'])
print(df2)

# 数量对应
s1 = pd.Series([3, 4, 5], index=datas[:3])  # 012
s2 = pd.Series([32, 5, 2], index=datas[1:])  # 123
df2['D'] = s1
df2['E'] = s2
print(df2)

# dropna去掉空行  注意需要
df3 = df2.dropna(axis=0, how='any')  # axis 0行 1列  how =any all  any任意一个 all全部  行内一个或多个空置就去掉对应行
print("dropna:", df3)

df3 = df2.dropna(axis=0, how='all')  # axis 0行 1列  how =any all  any任意一个 all全部  行内一个或多个空置就去掉对应行
print(df3)

df3 = df2.dropna(axis=1, how='any')  # axis 0行 1列  how =any all  any任意一个 all全部  行内一个或多个空置就去掉对应行
print(df3)

df3 = df2.fillna(value=0)  # 空值赋值0
print(df3)

df3 = df2.isnull()  # 查看空值
print(df3)

f = np.any(df2.isnull())  # 只要有一个空值就回返回true
print(f)

f = np.all(df2.isnull())  # 全部空值就回返回true
print(f)

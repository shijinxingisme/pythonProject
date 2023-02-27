'''
pandas复制及操作
'''

import numpy as np
import pandas as pd

datas = np.arange(20200101, 20200107)
df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=datas, columns=['A', 'B', 'C', 'D'])
print(df1)

# 赋值
print(df1.iloc[2, 2])
df1.iloc[2, 2] = 100  # 赋值
print(df1)
df1.loc[20200102, 'B'] = 200  # 类型对应
print(df1)
df1[df1.D > 11] = 0  # 找到D列大于10的行数 赋值 然后 把对应数据赋值为0打印
print(df1)
df1.A[df1.A == 0] = 1  # 找到A列=0的行 并把1赋值到A列 打印
print(df1)  # 索引中指定了就展示指定的行
df1['E'] = 10  # 展示对应列 没有则添加
print(df1)
df1['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=datas)  # 添加一列数据 到F列
print(df1)
df1.loc[20200107, ['A', 'B', 'C']] = [1, 2, 3]  # 添加一行数据到20200107 对应 ABC列 结果123  没有值NAN代替一
print(df1)

# iloc 是索引  loc是索引对饮的值
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=['A','B','C','D','E','F'])
s1.name = 'S1'
df2 = df1.append(s1)        #追加一行
# pd.concat(df1,s1)
print(df2)

df1.insert(2,'G',df2['E'])      #插入一列G 放到第三行 数据来源是 df2的E列
print(df1)

#移动列
g = df1.pop('G')  #弹出G列
print(df1)
df1.insert(6,'G',g)
print(df1)

#删除列
del df1['G']  #单列
print(df1)
df2 = df1.drop(['A','B'],axis=1)    #删除AB列  axis=1 列
# print(df1)
print(df2)

df2 = df1.drop([20200101,20200102],axis=0)  #删除行   axis=1 行
print(df1)
print(df2)

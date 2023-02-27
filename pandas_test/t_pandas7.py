'''plot 画图 '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()        #累加
# data.plot()
# plt.show()  #展示图

# 1000行4列
# a = np.random.randn(1000,4)
# print(a)

data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
data = data.cumsum()
print(data.head())  #前五行的值
# data.plot()     #绘图
# plt.show()      #展示

#散点图1
ax = data.plot.scatter(x='A',y='B',color='Blue',label='calss 1')
#散点图2  把1加入到2中 然后绘图
data.plot.scatter(x='A',y='C',color="Green",label="class 2",ax=ax)
plt.show()

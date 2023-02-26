import numpy as np

a = np.array([1,2,3],dtype=np.int32)
print(a.dtype)

b = np.array([1,2,3],dtype=float)
print(b.dtype)

d= np.array([[1,2,3],[4,5,6]])  #二维矩阵
print(d)

zero=np.zeros((2,3))    #生产2行3列全为0的矩阵
print(zero)

one = np.ones((3,4))     #生产2行3列全为1的矩阵
print(one)

emp = np.empty((3,2))   #生成 3行2列接近0的矩阵
print(emp)

e=np.arange(10)     #0-9的矩阵
print(e)

e=np.arange(4,10)     #4-9的矩阵
print(e)

e=np.arange(4,10,2)     #4-9的矩 间隔2
print(e)

#重新定义矩阵的形状
g = np.arange(10).reshape(2,5)  #一维数组 转换为 2行5列的矩阵
print(g)



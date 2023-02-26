import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[1, 1, 2], [2, 6, 6]])
# print(array1+array2)    #相同位置相加
# print(array1-array2)    #相减
# print(array1*array2)    #相称
# print(array1**array2)    #幂
# print(array1/array2)    #除法
# print(array1%array2)    #取余
# print(array1//array2)    #取整
# print(array1+1)    #都加1
# print(array1*10)    #都加1
# array3 =array1>3
# print(array3)
arr4 = np.ones((3, 5))
print(array1)  # 2-3
print(arr4)  # 3-5
#  2，5  行* 列  1行*1列 1行*2列...
#                2行*1列 2*2列 。。。
res = np.dot(array1, arr4)  # 矩阵乘法 array1 行， arr4列
print(res)

res2= array1.dot(arr4)
print(res2)

print(array1.T) #转置1
print(np.transpose(array1)) #转置2


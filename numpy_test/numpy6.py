'''
合并
'''

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.vstack((arr1,arr2))       #垂直合并
print(arr3)
print(arr3.shape)   #形状
arr4 = np.hstack((arr1,arr2))       #水平合并
print(arr4)
arr5 = np.vstack((arr1,arr2,arr3))  #多个数组合并
print(arr5)

arr = np.concatenate((arr1,arr2,arr1))
print(arr)
print("arr")
arr6 = np.concatenate((arr3,arr3),axis=0)   #axis=0 纵向合并 维度要相同 形状要匹配
print(arr6)
arr6 = np.concatenate((arr3,arr3),axis=1)   #axis=1  横向合并 维度要相同 形状要匹配
print(arr6)

print(arr1.T)   #一维array不能转置
print(arr1.shape)   #一维array形状  (3,)

arr1_1=arr1[np.newaxis,:]   #增加维度  到行
print(arr1_1)
print(arr1_1.shape)     #形状变为 一行3列 (1, 3)
print(arr1_1.T)     #增加维度后可以转置  转置后一行3列

arr1_2 = arr1[:,np.newaxis] #增加维度   到列
print(arr1_2)
print(arr1_2.shape)     # 3行一列
print(arr1_2.T)     # 转换后为一列 3行
print("=================")

arr1_3 = np.atleast_2d(arr1)    #转换为二维数据
print(arr1_3)
print(arr1_3.shape)
print(arr1_3.T)


arr1_4 = np.atleast_3d(arr1)    #转换为三维数据
print(arr1_4)
print(arr1_4.shape)
print(arr1_4.T)



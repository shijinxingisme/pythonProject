'''
分割
'''

import numpy as np

arr1= np.arange(12).reshape(3,4)    # 0-11  转成3*4的数二维组
print(arr1)
arr2,arr3 = np.split(arr1,2,axis=1) #水平方向分割 分成2份
print(arr2)
print(arr3)

arr4,arr5,arr6 = np.split(arr1,3,axis=0) #垂直方向分割 分成3份
print(arr4)
print(arr5)
print(arr6)

#分不出来报错
# arr2,arr3,arr4 = np.split(arr1,3,axis=1) #水平方向分割 分成3份
# print(arr2)
# print(arr3)
# print(arr4)

#切成三个部分不一定一样 array_split 不等分
arr7,arr8,arr9 = np.array_split(arr1,3,axis=1) #水平(列)方向分割 分成3份
print(arr7)
print(arr8)
print(arr9)

arr17,arr18,arr19 = np.vsplit(arr1,3) #垂直(行)方向分割 分成3份
print(arr17)
print(arr18)
print(arr19)


arr27,arr28 = np.hsplit(arr1,2) #垂直(行)方向分割 分成3份
print(arr27)
print(arr28)

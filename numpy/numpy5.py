'''
索引
'''

import numpy as np

arr1 = np.arange(2,14)      #生成2-14的数字
print(arr1)
print(arr1[2])          #2
print(arr1[2:5])        #2-5不包括5
print(arr1[2:-1])        #2-最后不包括最后
print(arr1[:5])        #0-5 不包括5
print(arr1[-5:])        #最后5个
arr2 = arr1.reshape(3,4)    #1维转为 3*4的二维数组
print(arr2)
print(arr2[1])
print(arr2[1][1])       #第一行第一列
print(arr2[1,2])        #第一行第二列
print(arr2[:,2])        #所有行第二列

for i in arr2:
    print(i)            #打印每一行

for i in arr2.T:
    print(i)        #打印每一列


for i in arr2.flat:     #扁平化
    print(i)



'''
浅拷贝 和 深拷贝
'''

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = arr1
arr2[0] = 5
# 值想同  共享内存  浅拷贝
print(arr1)
print(arr2)

arr3 = arr1.copy()  # 深拷贝
arr3[0]=10
print(arr1)
print(arr3)

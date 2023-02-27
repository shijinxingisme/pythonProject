import numpy as np

smple = np.random.random((3,2)) #随机 3行2列 0-1的随机数
print(smple)
s= np.random.normal(size=(3,2)) #3-2列 标准正态分布的随机数
print(s)

randomint = np.random.randint(0,10,size=(3,2)) #3-2 0-10的随机整数
print(randomint)
print(np.sum(randomint))    #求和
print(np.min(randomint))    #最大值
print(np.max(randomint))    #最小值
print(np.sum(randomint,axis=0)) #对列求和
print(np.sum(randomint,axis=1)) #对行求和
print(np.argmin(randomint)) #求最小值索引
print(np.argmax(randomint)) #求最大值索引
print(np.mean(randomint)) #求平均值
print(randomint.mean()) #求平均值
print(np.median(randomint)) #求中位数 双数取中间平均值 单数找中间
print(np.sqrt(smple)) #开方

inta = np.random.randint(0,10,size=(1,10))
print(inta)
print(np.sort(inta))        #排序 每一行
print(np.sort(smple))        #排序 每一行

print(np.clip(inta,2,7))    #小于2变成2 大于7的变成7 



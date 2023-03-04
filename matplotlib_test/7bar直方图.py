import numpy as np
import matplotlib.pyplot as plt

x= np.arange(10)
y=2**x +10
# 0 2 4 8 16 32 64 128 256 512
# 画一个直方图 实体红色 边框黑色
plt.bar(x,y,facecolor='red',edgecolor='black')
# zip可以组合xy一起遍历
for x,y in zip(x,y):
    #加上说明 %  占位符  .2f  两位浮点数
    # va='bottom' 显示在上面
    plt.text(x,y,'%.2f' % y,ha='center',va='bottom')
plt.show()

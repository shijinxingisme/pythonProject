import numpy as np
import matplotlib.pyplot as plt

# https://www.bilibili.com/video/BV1aa4y1i7kJ/?p=4&spm_id_from=pageDriver&vd_source=d45e7fa6827868e5c143d3c05fd5e52e
x=np.linspace(-3,3,100)
y1=2*x+1
y2=x**2

#xy范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#xy描述
plt.xlabel('this X')
plt.ylabel('this Y')

# linewidth 线宽度1  风格是 --
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
# linewidth 线宽度5  风格是 -
plt.plot(x,y2,color='blue',linewidth=8.0,linestyle='-')

# 创建数值序列工具 类似于arange  -2  到 2  一共生成11个均匀分布的数字
new_ticks = np.linspace(-2,2,11)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ['lv1','lv2','lv3','lv4','lv5'])

plt.show()

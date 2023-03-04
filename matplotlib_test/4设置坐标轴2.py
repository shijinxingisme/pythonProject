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
#gca 获取当前坐标轴
ax = plt.gca()
#设置坐标轴右边设置为红色
ax.spines['right'].set_color('none')
#设置坐标轴上边设置为红色
ax.spines['top'].set_color('none')
# 把X轴的刻度设置为bottom
ax.xaxis.set_ticks_position('bottom')
# 把y轴的刻度设置为left
ax.yaxis.set_ticks_position('left')
#设置bottom对应到 0点
ax.spines['bottom'].set_position(('data',0 ))
#设置left对应到 0点
ax.spines['left'].set_position(('data',0))

plt.show()

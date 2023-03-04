import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,100)
y1=2*x+1

# linewidth 线宽度1  风格是 -
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='-')

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

x0 = 0.5
y0 = 2*x0 +1
#画点  x0 yo 坐标 s大小
plt.scatter(x0,y0,s=50,color='b')
#画虚线  第一个参数x坐标(线)  第二个Y坐标(线) lw宽度
plt.plot([x0,x0],[y0,0],'r--',lw=5)
# r'$内容$' %2 占位符 % y0 对应值 xytext描述的位置 相对于x轴 y轴    textcoords 左边描述的点作为起点
plt.annotate(r'$2X+1=%s$' % y0,xy=(x0,y0), xytext=(+30,-30),textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
#
#   arrowprops=dict(arrowstyle='->') 箭头
# connectionstyle='arc3,rad=.2'  弧度

#xy位置 内容 \转义空格    fontdict文字属性 大小 颜色
plt.text(-2,2,r'$this\ is\ the\ text$',fontdict={'size':'10','color':'r'})

plt.show()


#https://blog.csdn.net/python1639er/article/details/112325519
#占位符  s 字符串  d 十进制  f十进制浮点数

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

'''动态图'''
fig,ax = plt.subplots()

x= np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))
# interval=20 图片间隔20毫秒

#返回Y值动态
def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,
#初始化函数
def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,func=animate,init_func=init,interval=20 )

plt.show()

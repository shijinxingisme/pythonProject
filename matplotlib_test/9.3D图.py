import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig= plt.figure()
ax = Axes3D(fig)

x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
#传入网格中
X,Y = np.meshgrid(x,y)
#Z坐标
R = np.sqrt(X**2+Y**2)
Z = np.sin(R)
# rstride=1 色块变大？ cstride=1  cmap 颜色 彩虹色
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))

#映射到底部   zdir='z'
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)

plt.show()

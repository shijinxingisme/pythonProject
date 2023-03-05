import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    # x y 对应的高度
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

x= np.linspace(-3,3,100)
y= np.linspace(-3,3,100)

# xy传入网格中 生成 XY
X,Y =np.meshgrid(x,y)
#contourf 绘制等高线   平均生成8+1条等高线
# alpha=0.75   混合值
#cmap=plt.cm.hot  热力图
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#黑色等高线C  线的宽度
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
#C的数值描述 inline=True在等高线里面 数值宽度
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())

plt.show()

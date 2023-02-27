import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-1,1,100)
y1=2*x+1
y2=x**2
# figure1
# plt.figure()
# plt.plot(x,y1)

#figure 2
# plt.figure()
# plt.plot(x,y2)

# 设置显示大小
# plt.figure(figsize=(8,5))
# plt.plot(x,y2)

# linewidth 线宽度1  风格是 --
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
# linewidth 线宽度5  风格是 -
plt.plot(x,y2,color='blue',linewidth=8.0,linestyle='-')
plt.show()

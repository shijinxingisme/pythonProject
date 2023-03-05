import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
#两行两列 位置1
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
#两行两列 位置2
plt.subplot(2,3,4)
plt.plot([0,1],[0,1])

plt.subplot(235)
plt.plot([0,1],[0,1])

plt.subplot(2,3,6)
plt.plot([0,1],[0,1])

plt.show()

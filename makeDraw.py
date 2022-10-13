"""
python绘图

"""

import matplotlib.pyplot as plt

from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x = np.random.randint(0,20,(20),np.int32)
# y = np.random.randint(0,20,(20),np.int32)
# z = np.random.randint(0,20,(20,20),np.int32)
#
# fig = plt.figure() # 画布
# ax = Axes3D(fig)  # 3d图形
# ax.plot_wireframe(x,y,z,cstride=1,rstride=1,color='green')  # 线框图
# plt.show()

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)
print(Z)
# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()


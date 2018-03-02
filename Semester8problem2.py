import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.mlab as mlabD
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


U0=10
a=100
restr = 100
length = a + 1

X = np.linspace(0, a, length)
Y = np.linspace(0, a, length)
Xgrid, Ygrid = np.meshgrid(X, Y)
Uset = np.zeros((length,length))
def U(x,y):
	potential = 0
	k=0
	while k <= restr:
		potential +=  4*U0/(np.pi*(2*k+1)) * ( np.cosh(y*(2*k+1)*np.pi/a) - 1/np.tanh((2*k+1)*np.pi)*np.sinh(y*(2*k+1)*np.pi/a)  )* np.sin(x*(2*k+1)*np.pi/a) 
		k += 1
	return potential

for i in range(length):
		for j in range(length):
			Uset[i][j]  = U(float(i),float(j))



fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(Xgrid, Ygrid, Uset, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0,U0)
ax.zaxis.set_major_locator(LinearLocator(6))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# CS = plt.contour(Xgrid, Ygrid, Uset,cmap=cm.coolwarm, colors = ('indigo', 'purple' , 'violet', 'aqua' ) , linewidths = 1)
# ax.plot_wireframe(Xgrid, Ygrid, Uset, color = 'black' ,linewidth = 0.3)
fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.clabel(CS, fontsize=9, inline=1)
# plt.title('U(x,y)')
# lab1 = 'potential'
# ax.set_xlabel(r'$Y$')
# ax.set_ylabel(r'$X$')

# ax.legend((lab1), loc='upper left')
# 
# 
plt.show()






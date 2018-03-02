import numpy as np
import matplotlib.pyplot as plt
import math
import imageio
import pylab
from mpl_toolkits.mplot3d import axes3d
import matplotlib
import matplotlib.mlab as mlabD
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

U0 = 100
class Solving:
    def __init__(self,M,N,eps):
        self.M = M
        self.N = N
        self.eps = eps
        self.Unew = np.zeros((M,N))
        self.Uold = np.ones((M,N))

    def Jacobi(self):  
        i=0
        while i< 1/self.eps:
            self.Uold = self.Unew
            self.Unew[1:self.M-1, 1:self.N-1] = (self.Uold[0:-2, 1:-1]+self.Uold[2:, 1:-1]+self.Uold[1:-1, 2:]+self.Uold[1:-1, 0:-2])/4
            self.Unew[:, 0] = 100
            self.Unew[self.M - 1, :] = 0
            self.Unew[0,:] = 0
            self.Unew[:, self.N - 1] = 0
            i+=1
        return self.Unew


    def plotter(self, U):
        x = np.linspace(0, self.M, self.M)
        y = np.linspace(0, self.N, self.N)
        xgrid, ygrid = np.meshgrid(x, y)
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(xgrid, ygrid, U, cmap=cm.coolwarm, linewidth=0, antialiased=False)        
        ax.set_zlim(0, 100)
        ax.zaxis.set_major_locator(LinearLocator(6))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    def run(self, method):
        if method == 'Jacobi':            
            self.plotter(self.Jacobi())

test = Solving(100, 100, 0.002)
test.run('Jacobi')  



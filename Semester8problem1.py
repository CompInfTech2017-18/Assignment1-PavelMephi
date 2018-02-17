
# coding: utf-8

# In[37]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class body:
    def __init__(self, m, V_x, V_y, F, plott, colour):
        self.V_x = V_x
        self.V_y = V_y
        self.mass = m
        self.gravity = F
        self.plott = plott
        self.colour = colour
   
    def position(self):
        t = np.linspace(0, 10, 100)
        x = self.evolveX(t)
        y = self.evolveY(t)
        plott.plot(x,y, 'r')
        
    def evolveX(self, t):
        return self.V_x * t
    
    def evolveY(self, t):
        return self.V_y * t - self.gravity* t**2 /(2.0*self.mass)
    
    
class rotator(body):
    def __init__(self, m, V_x, V_y, F, plott, colour, r, thi, w):
        self.radius = r
        self.angle = thi
        self.freq = w
        body.__init__(self, m, V_x, V_y, F, plott, colour)
        
    def evolve_rot_X(self, t,n):
        return self.V_x * t + (-1)**n *self.radius * np.cos(t*self.freq + self.angle)
    
    def evolve_rot_Y(self, t,n):
        return self.V_y * t - self.gravity* t**2 /(2.0*self.mass) + (-1)**n*self.radius * np.sin(t*self.freq + self.angle)
    
    def position_rot(self):      
        t = np.linspace(0, 10, 100)
        x = self.evolve_rot_X(t,0)
        y = self.evolve_rot_Y(t,0)
        plott.plot(x,y,self.colour)
        x = self.evolve_rot_X(t,1)
        y = self.evolve_rot_Y(t,1)
        plott.plot(x,y,self.colour)
    
class pplotter:    
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        
    def plot(self, x, y, colour):
        return self.ax.plot(x, y, colour)
    
    def show(self):
        plt.show()
        
plott = pplotter()
'ob = body(1.0,1.0,3.0,10.0,plott,'r')'

object = rotator(1.0, 1.0, 1.0, 10.0, plott, 'g', 1.0, 1.0, 0.5) 
object.position()
object.position_rot()



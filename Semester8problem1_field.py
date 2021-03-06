import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.lines as lines
class body:
    def __init__(self, m, V_x, V_y, F, plott, colour):
        self.V_x = V_x
        self.V_y = V_y
        self.mass = m
        self.gravity = F
        self.plott = plott
        self.colour = colour
   
    def position(self):
        t = np.linspace(0, 10, 20)
        x = self.evolveX(t)
        y = self.evolveY(t)
        plott.plot(x,y,'C1')
        
    def evolveX(self, t):
        return self.V_x * t
    
    def evolveY(self, t):
        return self.V_y * t - self.gravity* t**2 /(2.0*self.mass)

def system(y,t,coeff,a):
    phi, omega = y
    dy_dt = [omega, coeff*np.sin(phi)]
    return dy_dt
    
class rotator(body):
    def __init__(self, m, V_x, V_y, F, plott, colour, r, thi, omega, E, Q):
        body.__init__(self, m, V_x, V_y, F, plott, colour)
        self.radius = r
        self.angle = thi
        self.freq = omega
        self.field = E 
        self.charge = Q
        
    def ang_on_t(self,t):
        in_cod = [self.angle, self.freq]
        coeff = self.charge * self.field / (self.radius* self.mass)  
        return odeint(system,in_cod,t, args =(coeff,0))[:,0]

        
    def evolve_rot_X(self, t,n):
        return self.V_x * t + ((-1)**n)*self.radius*np.cos( self.angle) + ((-1)**n)*self.radius*np.cos(self.ang_on_t(t))
    
    def evolve_rot_Y(self, t,n):
        return self.V_y * t - self.gravity* t**2 /(2.0*self.mass) + ((-1)**n)*self.radius * np.sin( self.angle) + ((-1)**n)*self.radius*np.sin(self.ang_on_t(t))
    
    def position_rot(self):      
        t = np.linspace(0, 10, 30)
        x1 = self.evolve_rot_X(t,0)
        y1 = self.evolve_rot_Y(t,0)  
        l = plott.plot(x1,y1,'ro')
        plt.setp(l, markersize=10, markerfacecolor='g')
        x2 = self.evolve_rot_X(t,1)
        y2 = self.evolve_rot_Y(t,1)
        l2 = plott.plot(x2,y2,'ro')
        plt.setp(l2, markersize=10, markerfacecolor='r')
        for i in range(0,30):
            l3 = lines.Line2D([x1[i], x2[i]], [y1[i], y2[i]],  lw=2, color='black')
            plott.ax.add_line(l3)
        
    
class pplotter:    
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        
    def plot(self, x, y, colour):
        return self.ax.plot(x, y, colour)
    
    def show(self):
        plt.show()
        
plott = pplotter()


object = rotator(1., 2, 1, 0.5, plott, 'g', 1.0, np.pi/2, 0, 1., 0.05) 
object.position()
object.position_rot()
plt.show()

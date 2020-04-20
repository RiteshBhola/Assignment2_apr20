import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 


def fun(t,y):
	return(np.cos(2*t)+np.sin(3*t))

def g(t):
	return(np.sin(2*t)/2-np.cos(3*t)/3 + 4/3)
	
y0=1
h=0.01
tspan=np.arange(0,1+h,h)
n=tspan.size

sol=solve_ivp(fun,[tspan[0],tspan[n-1]],[y0],t_eval=tspan)
m=sol.y[0,:]
plt.plot(sol.t,m,"-k",label="From numpy.solve_ivp")
plt.plot(sol.t,g(sol.t),"-*r",label="From symbolic calculator")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
if(sol.status==-1):
 print("not converging")

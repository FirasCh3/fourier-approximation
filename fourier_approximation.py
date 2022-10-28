from scipy import signal
import matplotlib.pyplot as plot
import numpy as np
from math import*
def generate(t3,t):
    for i in range(1000):
        x=t[i]
        s=0
        k=1
        for j in range(19):
           s=s+((4/(pi*k))*(sin((pi*k*x)/0.1)))
           k=k+2
        t3.append(s)
t3=[]
t = np.linspace(0, pi/6, 1000, endpoint=True)
#plot.plot(t, signal.square(2 * np.pi * 5 * t))
plot.xlabel('x')
plot.ylabel('y')
generate(t3,t)
plot.plot(t,t3)




plot.show()

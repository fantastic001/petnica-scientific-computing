from lib import *
import matplotlib.pyplot as plt
import numpy as np 


n = int(input("Enter N: "))

m = [] 
i = [] 
g = 9.81 
r = 1 
dt = 1
theta = [] 
w = [] 
for k in range(n):
    mm = float(input("M of %d: " % k))
    ii = float(input("I of %d: " % k))
    ww = float(input("Angular velocity for %d: " % k))
    m.append(mm)
    i.append(ii)
    w.append(ww)
    ttt = float(input("theta of %d: " % k))
    theta.append(ttt)

m = np.array(m)
i = np.array(i)
theta = np.array(theta) 

y = []

for t in range(2000):
    y.append(theta) 
    theta, w = make_step(theta, dt, i, m, r, g, w)

plt.plot(y, np.sin(y))

plt.show()

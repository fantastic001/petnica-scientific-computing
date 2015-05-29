from lib import *
import matplotlib.pyplot as plt
import numpy as np 


n = int(input("Enter N: "))

m = [] 
i = [] 
g = 9.81 
r = 1 
dt = 0.01
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
T = 20
tt = np.arange(0, T, dt)
for t in tt:
    y.append(theta) 
    theta, w = make_step(theta, dt, i, m, r, g, w)

Y =[] 

for nn in range(n):
    yyy = []
    for time_period in y:
        yyy.append(time_period[nn])
    Y.append(yyy)

for nn in range(n):
    plt.figure()
    plt.plot(tt, np.sin(Y[nn]))

plt.show()

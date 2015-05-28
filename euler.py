import math 
import numpy as np 

import matplotlib.pyplot as plt 

dt = 0.001

def dy(t, y):
    return 2*y

y = []
t = np.arange(0, 20, dt)

for n in t:
    if n == 0: 
        y.append(1)
        continue
    y.append(y[-1] + dt*dy(n, y[-1]))

plt.plot(t,y)
plt.plot(t, math.e**(2*t))
plt.show()
b
#print(y)

import math 
import numpy as np 

import matplotlib.pyplot as plt 

dt = 0.1

def dy(t):
    return 2*t

y = []
t = np.arange(0, 20, dt)

for n in t:
    if n == 0: 
        y.append(0)
        continue
    y.append(y[-1] + dt*dy(n))

plt.plot(t,y)
plt.plot(t, t**2)
plt.show()
print(y)

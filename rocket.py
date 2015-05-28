import numpy as np 
import matplotlib.pyplot as plt 
import math

G = 6.67e-11

h = 0.001
def calculate_acc(x, t):
    m = 2
    -(G*m/(x[0]**2 + x[1]**2)) * (x/match.sqrt(x.dot(x)))


def gravity(x, t):
    return np.array([0, -9.81])

def compute_path(x0, v0, a, t, dt):
    x = []
    v = []
    for i in np.arange(0, t, dt):
        if i == 0:
            x.append(x0)
            v.append(v0)
            continue 
        v.append(v[-1] + dt*a(x[-1], t))
        x.append(x[-1] + np.array(v[-1])*dt)
    return x 

x0 = np.array([0,0])
v0 = np.array([1,1])

x = compute_path(x0, v0, gravity, 100, 0.01)
print(x)

xt = []
yt = [] 

for n in x: 
    if n[1] < 0:
        break
    xt.append(n[0])
    yt.append(n[1])

plt.plot(xt,yt, "o")

plt.show()

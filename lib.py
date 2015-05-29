
import math 
import numpy as np 
import matplotlib.pyplot as plt

def pre_plot_points(x):
    xt = [] 
    yt = []
    for n in x: 
        #if n[1] < 0:
        #    break
        xt.append(n[0])
        yt.append(n[1])
    return (xt, yt)

def compute_path(x0, v0, a, t, dt):
    """
    Computes path for given parameters 

    x0: initial starting point
    v0: initial velocity vector
    a: acceleration function which takes two args: position as np.array and time as float
    t: time period
    dt: step 
    """
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

def vector_direction(x):
    """
    Determines direction which is unit vector in the direction of given vector x 
    
    x: vector to determine direction
    """
    return x / (math.sqrt(x.dot(x)))

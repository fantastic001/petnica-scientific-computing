
import numpy as np 
import matplotlib.pyplot as plt 
import math 
import numpy.linalg as la 
def df(x):
    return np.array([2*x[0], 2*x[1]])

x = np.array([100, 100])

def ddf(x):
    return np.array([[2 , 0] , [0, 2]])

for i in range(1000):
    x += - np.dot(df(x), la.inv(ddf(x)))

print(x)


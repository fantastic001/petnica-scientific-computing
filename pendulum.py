from lib import make_matrix 

n = input("Enter N: ")

m = [] 
i = [] 
g = 9.81 
r = 1 
dt = 1
theta = [] 

for k in range(n):
    mm = input("M of %d: " % k)
    ii = input("I of %d: " % k)
    m.append(mm)
    i.append(ii)
    ttt = input("theta of %d: " % k)
    theta.append(ttt)

m = np.array(m)
i = np.array(i)
theta = np.array(theta) 

y = []

for t in range(2000):
    y.append(theta) 
    theta = make_step(theta, dt, i, m, r, g)



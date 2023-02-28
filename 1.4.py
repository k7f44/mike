import numpy as np 
a = np.array([[5,4], [2, -6]])
b = np.array([[14], [-2]]) 
c= np.linalg.solve(a, b)
print(c)
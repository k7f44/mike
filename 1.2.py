import numpy as np 
a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2]) 
print (a.shape)

are = a.reshape ((9,1))
print(are)

arc = a.reshape ((3,3))
print(arc)

max1 = arc.max(axis = 0)
print(max1)

max2 = arc.max(axis = 1)
print(max2)

min1=arc.min(axis = 0)
print(min1)

min2=arc.min(axis = 1)
print(min2)

min3=arc.sum(axis = 0)
print(min3)

min4=arc.sum(axis = 1)
print(min4)

import numpy as np 
a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2]) 
print (a.shape)

are = a.reshape ((9,1))
print(are)

arc = a.reshape ((3,3))
print(arc)

max1 = arc.max(axis = 0)
print(max1)

max2 = arc.max(axis = 1)
print(max2)

min1=arc.min(axis = 0)
print(min1)

min2=arc.min(axis = 1)
print(min2)

min3=arc.sum(axis = 0)
print(min3)

min4=arc.sum(axis = 1)
print(min4)

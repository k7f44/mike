import numpy as np 
a = np.array([[2.3, 5.1, 4.7], [3.5, 6.7, 1.5],  [8.4, 3.1, 9.2]]) 
b = np.array([[4.3, 8.1, 6.1], [3.7, 6.2, 1.5], [2.4, 5.7, 4.7]]) 

aa=a.shape
print(aa)

print (a+b)
print (a-b)
print (a*b)
print (a/b)

print (a**2)

print ('___1.3_____')
print (b%2)

print (np.sin(b))
print (np.cos(a))
print (np.sin(b)+np.cos(b))
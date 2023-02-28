import numpy as np 
a = np.array([[2,8], [1, -6]])
b = np.array([[3,2,7], [4,1,8] , [6,3,7]])
c = np.array([[4,3,2,7], [6,1,1,-2],[7,5,8,1],[9,5,-3,-5]])

a1=np.transpose(a)
print(a1)
b1=np.transpose(b)
print(b1)
c1=np.transpose(c)
print(c1)

a2=np.linalg.inv(a) 
print('obr=',a2)
b2=np.linalg.inv(b) 
print('obr=',b2)
c2=np.linalg.inv(c) 
print('obr=',c2)

a3=np.linalg.det(a) 
print('opr=', a3)
b3=np.linalg.det(b) 
print('opr=', b3)
c3=np.linalg.det(c) 
print('opr=', c3)

b5=np.split(b, 3, axis=0)
#print(b5)

b6=np.linalg.norm(b, axis=1) 
print('norma vektorov = ' , b6)

c6=np.linalg.norm(c, axis=1) 
print('norma vektorov =',c6)
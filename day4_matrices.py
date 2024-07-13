import numpy as np

#random matrices generation using nparray
a=np.random.randint(10,size=(3,3))
b=np.random.randint(20,size=(3,3))
print(a)
print('\n')
print(b)


#addition of matrices
c=a+b
print("Addition :")
print(c)
print('\n')


#Subtraction of matrices
d=a-b
print("Subtraction :")
print(d)
print('\n')

#Scaler Multiplication of matrices
e=a*2
f=b*2
print('Scaler Multiplication :')
print("a*2 :\n")
print(e)
print('\n')
print("b*2 :\n")
print(f)
print('\n')


#Multiplication of matrices

print("Multiplication : a*b")
g=np.matmul(a,b)
print(g)
print('\n')
tran_a=np.transpose(a)
print(a)
print(f"Transpose of a :\n {tran_a}")

import numpy as np
from math import factorial
# np.random.seed(1)
# n = 60
# b = np.random.randint(1,7,n)
# print(b)
# a = b [b==3]
# print(a)
# m = len(a)
# print(m)
# w = m/n
# print(w)

# np.random.seed(1)
# n = 360
# c = np.random.randint(1,7,n)
# d = np.random.randint(1,7,n)
# # print(c)
# # print(b)
# a = c[(c==1) & (d==2)]
# print(a)
# m = len(a)
# print(m)
# w = m/n
# print(w)
''' Комбинации'''
def combination (n, k):
    return factorial(n) // (factorial(k) * factorial(n - k ))
print(combination( 36, 4))

'''Размещение'''
def arrangements (n, k):
    return factorial(n) // factorial (n - k)
print(arrangements( 20, 5))    

'''Перестановки'''

def permutation(n):
    return factorial(n)
print(permutation(5))      
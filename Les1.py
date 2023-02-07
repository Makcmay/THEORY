import numpy as np
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
np.random.seed(1)
n = 360
c = np.random.randint(1,7,n)
d = np.random.randint(1,7,n)
# print(c)
# print(b)
a = c[(c==1) & (d==2)]
print(a)
m = len(a)
print(m)
w = m/n
print(w)
import numpy as np
import math as mt


def combination (n, k):
    return mt.factorial(n) // (mt.factorial(k) * mt.factorial(n - k ))

def bern(n, p, k):
    return combination(n, k) * np.power(p, k) * np.power((1 - p), (n - k))

'''
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
Стрелок выстрелил 100 раз. 
Найдите вероятность того, что стрелок попадет в цель ровно 85 раз
'''
# p = 0.8
# n = 100
# k = 85


print(bern(100, 0.8, 85))

'''
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
Какова вероятность, что ни одна из них не перегорит в первый день? 
Какова вероятность, что перегорят ровно две?
'''
m1 = 0
m2 = 2
n = 5000
p =0.0004
lam = n * p

def poisson(m, lam):
    return np.power(lam, m) // mt.factorial(m) * mt.exp(-lam)

print(poisson(m1, lam))
print(poisson(m2, lam))

'''
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
'''
# n = 144
# k = 70
# p = 0.5

print(bern(144, 0.5, 70))

'''
В первом ящике находится 10 мячей, из которых 7 - белые. 
Во втором ящике - 11 мячей, из которых 9 белых. 
Из каждого ящика вытаскивают случайным образом по два мяча. 
Какова вероятность того, что все мячи белые? 
Какова вероятность того, что ровно два мяча белые? 
Какова вероятность того, что хотя бы один мяч белый?
'''

print(f'вероятность того, что все мячи белые = {combination(7, 2) / combination(10, 2) * combination(9, 2) / combination(11, 2)}')

a = combination(7, 2) / combination(10, 2) * combination(2, 2) / combination(11, 2)
b = combination(7, 1) * combination(3, 1) / combination(10, 2) * combination(9, 1) * combination(2, 1)/ combination(11, 2)
c = combination(3, 2) / combination(10, 2) * combination(9, 2) / combination(11, 2)
print(f'вероятность того, что ровно два мяча белые = {a + b + c}')

d = combination(3, 2) / combination(10, 2) * combination(2, 2) / combination(11, 2)
print(f'вероятность того, что хотя бы один мяч белый = {1 - d}')
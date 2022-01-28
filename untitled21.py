# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 09:33:20 2021

@author: user
"""
# x = list(range(1,5,3))
# n = list(range(0,2))
# sonlar = []
# for son in x:
#     for son_1 in n:
#         sonlar.append(son*(2**son_1))
# print(sum(sonlar))


x = 1
n = 0
sonlar = []
while True:
    sonlar.append((2**n)*x)
    x = x + 3
    n = n + 1
    if x == 70 and n == 23:
        break

print(sum(sonlar))







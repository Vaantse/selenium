# -*- coding:utf-8 -*-
import openpyxl
__author__ = "Cydonia"
from functools import reduce

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(6))

def factorial(n):
    return reduce(lambda x, y: x * y, list(range(1, n+1)))

print(factorial(6))
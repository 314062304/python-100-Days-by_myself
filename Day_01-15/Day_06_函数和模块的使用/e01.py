#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  求阶乘  """

def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(factorial(n) // factorial(m) // factorial(m - n))
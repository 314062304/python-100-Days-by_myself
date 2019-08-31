#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  用for循环实现1~100之间的偶数求和  """

sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)
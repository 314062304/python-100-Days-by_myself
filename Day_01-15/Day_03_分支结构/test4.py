#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 判断输入的边长能否构成三角形 如果能则计算出三角形的周长和面积 """

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c >b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % area)
else:
    print('不能构成三角形')


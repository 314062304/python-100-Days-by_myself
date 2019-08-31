#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  摇色子  """

from random import randint

def roll_dice(n=2):           # n: 色子的个数
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total                # return: n颗色子点数之和

def add(a=0, b=0, c=0):   # return: n颗色子点数之和
    return a + b + c

print(roll_dice())      # 如果没有指定参数，那么使用默认值摇两颗骰子

print(roll_dice(3))     # 摇三色骰子
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

print(add(c=50, a=100, b=200))  # 传递参数时可以不按照设定的顺序进行传递
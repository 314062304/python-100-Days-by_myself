#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 掷骰子决定做什么事情 """

from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱个歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲笑话'

print(result)
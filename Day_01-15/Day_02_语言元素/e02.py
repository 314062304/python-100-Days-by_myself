#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""     使用input()函数获取键盘输入 使用int()进行类型转换 用占位符格式化输出的字符串     """

a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))      # %%为转义符
print('%d ** %d 9= %d' % (a, b, a ** b))
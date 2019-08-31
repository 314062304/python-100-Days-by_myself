#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  写一个程序判断输入的正整数是不是回文素数  """

from test2 import is_palindrome
from test3 import is_prime

if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)
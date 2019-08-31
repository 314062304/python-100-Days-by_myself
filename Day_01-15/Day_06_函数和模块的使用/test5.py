#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  Python中有关变量作用域的问题

    Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索
"""

def foo():
    # b是局部变量，数据局部作用域，在foo函数外无法访问
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        # c是局部变量，属于局部作用域，在bar函数外无法访问
        c = True
        print(a)
        # 对于bar函数，b属于嵌套作用域
        print(b)
        print(c)

    bar()

if __name__ == '__main__':
    # a是一个全局变量（global variable），属于全局作用域
    a = 100
    foo()
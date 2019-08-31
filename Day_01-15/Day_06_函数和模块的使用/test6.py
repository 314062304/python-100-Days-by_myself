#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def foo():
    # 调用、修改全局变量
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200



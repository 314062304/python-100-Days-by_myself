#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  访问可见性问题  """

class Test:
    def __init__(self, foo):
        # __foo属性为私有属性：在给属性命名时可以用两个下划线作为开头
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    # 私有属性无法调用
    # test.__bar()
    # print(test.__foo)

    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
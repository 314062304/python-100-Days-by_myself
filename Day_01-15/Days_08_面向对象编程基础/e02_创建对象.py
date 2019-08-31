#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  创建对象  """
from e01_定义类 import Student
def main():
    #
    stu1 = Student('阿良', 25)
    #
    stu1.study('Python程序设计')
    #
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
    main()
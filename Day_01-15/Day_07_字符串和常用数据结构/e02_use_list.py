#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  使用列表  """

def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)

    # 计算列表长度(元素个数)
    print(len(list1))

    # 下标(索引)运算
    print(list1[0])
    print(list1[4])
    # print(list1[5]) # IndexError: list index out of range
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300
    print(list1)

    # 添加元素
    list1.append(200)           # 迭代
    list1.insert(1, 400)        # 在存在的元素后边加入新元素
    list1 += [1000, 2000]       # 迭代
    print(list1)
    print(len(list1))

    # 删除元素
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)

    # 清空列表元素
    list1.clear()
    print(list1)


if __name__ == '__main__':
    main()
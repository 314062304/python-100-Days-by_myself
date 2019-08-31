#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  使用集合  """

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))

    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)

    # remove的元素如果不存在会引发Keyerror
    if 4 in set2:
        set2.remove(4)
    print(set2)

    # 遍历集合容器
    for val in set2:
        print(val ** 2, end=' ')
    print()

    # 将元组转换成集合
    tuple1 = (1, 2, 3, 3, 2, 1)
    set3 = set(tuple1)
    print(set3.pop())
    print(set3)

    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    print(set1.intersection(set2))

    print(set1 | set2)
    print(set1.union(set2))

    print(set1 - set2)
    print(set1.difference(set2))

    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))

    # 判断子集和超集
    print(set2 <= set1)
    print(set2.issubset(set1))

    print(set3 <= set1)
    print(set3.issubset(set1))

    print(set1 >= set2)
    print(set1.issuperset(set2))

    print(set1 >= set3)
    print(set1.issuperset(set3))




if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""   使用字典  """

# 字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。

def main():
    history_dict = {'阿良': 95, '白元芳': 78, '狄仁杰': 82}

    # 通过键可以获得字典中对应的值
    print(history_dict['阿良'])
    print(history_dict['狄仁杰'])

    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in history_dict:
        print('%s\t --->\t%d' % (elem, history_dict[elem]))

    # 更新字典中的元素
    history_dict['白元芳'] = 65
    history_dict['诸葛孔明'] = 80
    history_dict.update(冷面=67, 方启鹤=85)
    print(history_dict)
    if '武则天' in history_dict:
        print(history_dict['武则天'])
    print(history_dict.get('武则天'))

    # get方法也是通过键获取对应的值但是可以设置默认值
    print(history_dict.get('武则天', 60))

    print(history_dict)

    # 删除字典中的元素
    print(history_dict.popitem())
    print(history_dict.popitem())
    print(history_dict.pop('阿良', 100))

    # 清空字典
    history_dict.clear()
    print(history_dict)

if __name__ == '__main__':
    main()
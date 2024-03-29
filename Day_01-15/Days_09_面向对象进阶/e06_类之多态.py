#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  类之间的关系 - 多态"""

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """  宠物  """

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_vocie(self):
        """  发出声音  """
        pass


class Dog(Pet):
    """  狗  """

    def make_vocie(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """  猫  """

    def make_vocie(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_vocie()

if __name__ == '__main__':
    main()
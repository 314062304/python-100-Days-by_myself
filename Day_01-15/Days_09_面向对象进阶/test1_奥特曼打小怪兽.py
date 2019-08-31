#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  奥特曼打小怪兽  """

# time.sleep(1)是为了方便观看游戏过程，避免直接出结果

import time
from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """  战斗者  """
    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """  初始化方法  """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """  攻击  other：被攻击的对象"""
        pass


class Ultraman(Fighter):
    """  奥特曼  """

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """  初始化方法  """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other._hp -= randint(15, 25)

    def huge_attack(self, other):
        """  究极必杀技(打掉对方至少50点或四分之三的血)  """

        if self._mp >= 50:
             self._mp -= 50
             injury = other.hp * 3 // 4
             injury = injury if injury >= 50 else 50
             other.hp -= injury
             return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """   魔法攻击  """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True     # 使用魔法成功
        else:
            return False    # 使用魔法失败

    def resume(self):
        """  恢复魔法值  """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + '生命值：%d\n' % self._hp + '魔法值：%d' % self._mp



class Monster(Fighter):
    """  小怪兽  """

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    """  判断有没有小怪兽是活着的  """
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """  选中一只活着的小怪兽  """
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """  显示奥特曼和小怪兽的信息  """
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('阿良', 2000, 500)
    m1 = Monster('泰坦巨猿', 800)
    m2 = Monster('巨眼魔蛛', 350)
    m3 = Monster('双头狼', 300)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=======第%02d回合=======' % fight_round)
        m = select_alive_one(ms)        # 选中一只小怪兽
        skill = randint(1, 10)          # 通过随机数选择使用哪种技能
        if skill <= 6:      # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s。' % (u.name, m.name))
            time.sleep(1)
            u.attack(m)
            print('%s的魔法值恢复了%d点。' % (u.name, u.resume()))
            time.sleep(1)
        elif skill < 9:     # 30%的概率使用魔法攻击（可能以内魔法值不足而失败）
            if u.magic_attack(ms):
                print('%s使用了魔法攻击。' % u.name)
                time.sleep(1)
            else:
                print('%s使用魔法失败。' % u.name)
                time.sleep(1)
        else:               # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s' % (u.name, m.name))
                time.sleep(1)
            else:
                print('%s使用普通攻击打了%s' % (u.name, m.name))
                time.sleep(1)
                print('%s的魔法值恢复了%d点' % (u.name, u.resume()))
                time.sleep(1)
        if m.alive > 0:
            print('%s回击了%s' % (m.name, u.name))
            time.sleep(1)
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n=======战斗结束！=======\n')
    time.sleep(1)
    if u.alive > 0:
        print('%s奥特曼胜利！' % u.name)
        time.sleep(1)
    else:
        print('小怪兽胜利！')
        time.sleep(1)


if __name__ == '__main__':
    main()

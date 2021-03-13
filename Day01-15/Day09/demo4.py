from abc import ABCMeta, abstractmethod
from random import *


class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @abstractmethod
    def attack(self, other):
        """
        抽象方法
        攻击
        other；被攻击对象
        """
        pass


class Ultraman(Fighter):
    """
      初始化方法

     :param name: 名字
     :param hp: 生命值
     :param mp: 魔法值
      """
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    """攻击 并返回攻击值"""

    def attack(self, other):
        depoint = randint(10, 20)
        other.hp -= depoint
        return depoint

    def huge_attack(self, other):
        """
               究极必杀技(打掉对方至少50点或四分之三的血)

               :param other: 被攻击的对象

               :return: 使用成功返回True否则返回False
         """
        if self._mp >= 50:
            self._mp = 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param others:被攻击的群体
        :return: 使用魔法成功返回True否则返回False，并返回伤害值
        """
        depoint = 0
        isaffect = False
        if self._mp >= 20:
            self._mp -= 20
            depoint = randint(10, 15)
            for temp in others:
                if temp.alive:
                    temp.hp -= depoint
                    isaffect = True
            return (isaffect, depoint)
        else:
            return (isaffect, depoint)

    def resume(self):
        """
        恢复魔法值
        :return:
        """
        incipient = randint(1, 10)
        self._mp += incipient
        return incipient

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + '生命值：%d\n' % self._hp + '魔法值：%d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        depoint = randint(10, 20)
        other.hp -= depoint
        return depoint

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


if __name__ == "__main__":
    u = Ultraman('奥特曼11', 500, 100)
    m1 = Monster('怪兽1', 200)
    m2 = Monster('怪兽2', 200)
    ms = [m1, m2]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        skill = randint(1, 10)
        m = select_alive_one(ms)
        if skill <= 8:
            depoint = u.attack(m)
            print('%s使用普通攻击打了%s. 伤害值：%d' % (u.name, m.name, depoint))
        elif skill <= 9:

            (isaffect, depoint) = u.magic_attack(ms)
            if isaffect:
                print('%s使用了魔法攻击.伤害值:%d' % (u.name, depoint))
            else:
                print('%s使用魔法失败.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            depoint = m.attack(u)
            print('%s回击了%s. 伤害值：%d' % (m.name, u.name, depoint))
        display_info(u, ms)

        print('\n========第%d回合战斗结束!========\n' % fight_round)
        fight_round += 1
    if u.alive > 0:
        print('%s胜利!' % u.name)
    else:
        print('小怪兽胜利!')

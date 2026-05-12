import random
from .creature import Creature
from enum import IntEnum

class Monster(Creature):
    class Type(IntEnum):
        DRAGON = 0
        ORC = 1
        SLIME = 2
        MAX_TYPES = 3

    __monster_data = [
        Creature("dragon", 'D', 20, 4, 100),
        Creature("orc", 'o', 4, 2, 25),
        Creature("slime", 's', 1, 1, 10)
    ]

    assert len(__monster_data) == Type.MAX_TYPES

    def __init__(self, monster_type: Type):
        data = self.__monster_data[monster_type]
        super().__init__(data.name, data.symbol, data.health,
                         data.damage, data.gold)

    @staticmethod
    def get_random_monster():
        random_type = random.randint(0, Monster.Type.MAX_TYPES - 1)
        return Monster(Monster.Type(random_type))


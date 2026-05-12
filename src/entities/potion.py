import random
from enum import IntEnum

class Potion:
    class Type(IntEnum):
        POISON = 0
        STRENGTH = 1
        HEALTH = 2
        MAX_TYPES = 3

    class Size(IntEnum):
        SMALL = 0
        MEDIUM = 1
        LARGE = 2
        MAX_SIZES = 3

    __poison_names = ["poison", "strength", "health"]
    __poison_size_names = ["small", "medium", "large"]

    assert len(__poison_names) == Type.MAX_TYPES
    assert len(__poison_size_names) == Size.MAX_SIZES

    def __init__(self, potion_type: Type, size: Size):
        self.__type = potion_type
        self.__size = size

    @property
    def type(self) -> Type:
        return self.__type

    @property
    def size(self) -> Size:
        return self.__size

    def get_name(self) -> str:
        return self.__poison_names[self.__type]

    def get_size_name(self) -> str:
        return self.__poison_size_names[self.__size]

    @staticmethod
    def get_random_potion():
        return Potion(Potion.Type(random.randint(0, Potion.Type.MAX_TYPES - 1)),
                      Potion.Size(random.randint(0, Potion.Size.MAX_SIZES - 1)))

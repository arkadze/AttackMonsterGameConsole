from .creature import Creature
from .potion import Potion

class Player(Creature):
    def __init__(self, name: str):
        super().__init__(name, '@', 10, 1, 0)
        self._level = 1
        print(f"Welcome, {name}")

    @property
    def level(self) -> int:
        return self._level

    def level_up(self):
        self._level += 1
        self._damage += 1

    def has_won(self) -> bool:
        return self._level >= 20

    # def is_dead(self):


    def drink_potion(self, p: Potion):
        match p:
            case Potion.Type.POISON:
                self.reduce_health(1)
            case Potion.Type.STRENGTH:
                self._damage += 1
            case Potion.Type.HEALTH:
                self._health += 5 if (p.size == Potion.Size.LARGE) else 2
            case _:
                print(f"The potion is gone.\n")

    def __str__(self):
        return (f"\nLevel: {self._level}, Damage: {self._damage}, "
                f"Health: {self._health}, Gold: {self._gold}\n")

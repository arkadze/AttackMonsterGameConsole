from dataclasses import dataclass

@dataclass(slots=True)
class Creature:
    _name: str
    _symbol: str
    _health: int
    _damage: int
    _gold: int

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def health(self) -> int:
        return self._health

    @property
    def gold(self) -> int:
        return self._gold

    @property
    def damage(self) -> int:
        return self._damage

    def reduce_health(self, damage: int):
        self._health -= damage

    def is_dead(self) -> bool:
        return self._health <= 0

    def add_gold(self, gold: int):
        self._gold += gold

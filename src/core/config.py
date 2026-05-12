from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    FLEE_SUCCESS_CHANCE: int = 50
    POTION_CHANCE: int = 30
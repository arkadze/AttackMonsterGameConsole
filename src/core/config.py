from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    POTION_CHANGE: int = 30
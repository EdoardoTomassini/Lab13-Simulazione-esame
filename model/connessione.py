from dataclasses import dataclass

from model.state import State


@dataclass
class Connessione:
    s1: State
    s2: State
    N: int

    def __str__(self):
        return f"{self.s1.Name}"

    def __hash__(self):
        return hash(self.s1.id)
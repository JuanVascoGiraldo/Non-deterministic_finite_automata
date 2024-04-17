from pydantic import BaseModel
from typing import Callable, Optional

class Automaton(BaseModel):

    states: list[str]
    alphabet: list[str]
    sigma: dict
    initial: str
    final: list[str]
    actual: Optional[list[str]] = [initial]

    def exist_status(self, status: str)-> bool:
        exist = next((x for x in self.states if x==status),None)
        if not exist:
            return False
        return True

    def set_actual_status(self, status: list[str]):
        exist = next((j for j in status if  self.exist_status(j)==False), True)
        if not exist:
            return None
        self.actual = status
        return True

    def change_state(self, letter: str):
        if len(self.actual) == 0:
            return True
        if len(letter)>1:
            return None
        for:
        
        if len(new_state) == 0:
            self.actual = ""
            return True
        return self.set_actual_status(new_state)

    def is_final(self):
        return next((x for x in self.final if x==self.actual),None)
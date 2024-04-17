from pydantic import BaseModel
from typing import Dict

class Automaton(BaseModel):

    states: list[str]
    alphabet: list[str]
    sigma: Dict[str, Dict[str, list[str]]]
    initial: str
    final: list[str]
    actual: list[str]

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
        new_states = []
        for state in self.actual:
            new_states.extend(self.sigma[state][letter] if letter in self.sigma[state] else [])
        
        for state in self.actual:
            new_states.extend(self.sigma[state]['epsilon'] if 'epsilon' in self.sigma[state] else [])
        
        new_states = set(new_states)
        if len(new_states) == 0:
            self.actual = []
            return True
        return self.set_actual_status(new_states)

    def is_final(self):
        for state in self.actual:
            if state in self.final:
                return True
        return False
    
    def get_epsilon_lock(self, state: str):
        lock = []
        if 'epsilon' in self.sigma[state]:
            lock.extend(self.sigma[state]['epsilon'])
        lock.append(state)
        return lock
    
    def get_all_epsilon_lock(self):
        lock = {}
        for state in self.states:
            lock[state] = self.get_epsilon_lock(state)
        lock["∅"] = ["∅"]
        return lock

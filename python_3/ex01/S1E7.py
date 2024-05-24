from typing import Any
from S1E9 import Character


class Baratheon(Character):
    """Respresinting Lannister Genes"""

    def __init__(self, first_name, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive)
        self.eyes = 'brown'
        self.hairs = 'light'
        self.family_name = "Baratheon"

    def die(self):
        """object method"""
        self.is_alive = False

    def __getattribute__(self, name: str) -> Any:
        if name == "__str__":
            return f"<bound method {self.__class__.__name__}.__str__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
        elif name == "__repr__":
            return f"<bound method {self.__class__.__name__}.__repr__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
        else:
            return super().__getattribute__(name)

   
class Lannister(Character):
    """Respresinting Lannister Genes"""

    def __init__(self, first_name, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive)
        self.eyes = 'blue'
        self.hairs = 'light'
        self.family_name = 'Lannister'

    def die(self):
        """instance methode"""
        self.is_alive = False

    def __getattribute__(self, name: str) -> Any:
        print(name)
        if(name == "__str__"):
            return "hey"
        return super().__getattribute__(name)

    def __getattribute__(self, name: str) -> Any:
        if name == "__str__":
            return f"<bound method {self.__class__.__name__}.__str__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
        elif name == "__repr__":
            return f"<bound method {self.__class__.__name__}.__repr__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
        else:
            return super().__getattribute__(name)

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class methode"""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
    

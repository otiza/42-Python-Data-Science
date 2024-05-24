from abc import ABC, abstractmethod


class Character(ABC):
    """class abstraction"""
    first_name:   str
    is_alive:   bool

    @abstractmethod
    def __init__(self, first_name, is_alive=True) -> None:
        """abstract constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """abstract methode"""
        pass


class Stark(Character):
    """Class impl"""
    def __init__(self, first_name, is_alive=True):
        """constructor impl"""
        super().__init__(first_name, is_alive)

    def die(self):
        """methode impl"""
        self.is_alive = False


class calculator:

    def __init__(self,vector) -> None:
        self.vector = vector

    def __add__(self,object) -> None:
        for idx , x in enumerate(self.vector):
            self.vector[idx] = x + object
        print(self.vector)


    def __mul__(self, object) -> None:
        for idx, x in enumerate(self.vector):
            self.vector[idx] = x * object
        print(self.vector)

    def __sub__(self, object) -> None:
        for idx, x in enumerate(self.vector):
            self.vector[idx] = x - object
        print(self.vector)


    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError
        for idx, x in enumerate(self.vector):
            self.vector[idx] = x / object
        print(self.vector)

    





        
        


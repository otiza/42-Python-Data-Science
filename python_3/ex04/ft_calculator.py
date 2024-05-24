
class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product = 0
        for idx, x in  enumerate(V1):
            product = product + x * V2[idx]
        print(product)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        for idx, x in enumerate(V1):
            V1[idx] = x + V2[idx]
        print(f"Add Vector is : {V1}")
        

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        for idx, x in  enumerate(V1):
            V1[idx] = x - V2[idx]
        print(f"Add Vector is : {V1}")

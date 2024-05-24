


def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    
    def inner() -> float:
        nonlocal count
        lcl_count = 0
        count += 1
        inner_x = x
        while(lcl_count < count):
            inner_x = function(inner_x)
            lcl_count += 1
        return inner_x
    return inner

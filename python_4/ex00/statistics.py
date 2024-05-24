from typing import Any

def mean(numbers : Any):
    mean = 0.0
    for num in numbers:
        mean = mean + num
    mean = mean / len(numbers)
    print(f'mean : {mean}')

def median(numbers: Any):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        print((numbers[length//2] + numbers[length//2 - 2]) / 2)
    else:
        print(f'median : {numbers[length //2]}')
    
def quartile(numbers: Any):
    numbers.sort()
    Qlength = len(numbers) //4
    Q1 = 0.0 + numbers[Qlength]
    Q2 = 0.0 + numbers[Qlength * 3]

    print(f'quartile : {[Q1,Q2]}')


def std(numbers: Any):
    length = len(numbers)
    mean = 0.0 + sum(numbers) / length
    total = 0.0
    for x in numbers:
        total = total + (x - mean)** 2
    print(f'std : {(total/length) ** .5}')

def var(numbers: Any):
    length = len(numbers)
    mean = 0.0 + sum(numbers) / length
    total = 0.0
    for x in numbers:
        total = total + (x - mean)** 2
    print(f'var : {(total/length)}')
    

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    util_map = {
        "mean" : mean,
        "quartile" : quartile,
        "median" : median,
        "std" : std,
        "var" : var,
    }
    
    for func in kwargs:
        if kwargs[func] in util_map.keys():
            try:
                util_map[kwargs[func]](list(args))
            except:
                print("ERROR")
        else:
            pass
        
    
            


# ft_statistics(1, 42, 360, 11,64, toto="mean", tutu="median", tata="quartile")




    # print(variance * variance)


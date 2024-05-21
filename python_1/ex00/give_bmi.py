

def printError(e):
    """
    takes an exception and print it to the stderr formatted
    """
    print(type(e).__name__ + ": " + str(e))

def give_bmi(height: list[int | float], weight: list[int | float]):
    """Calculate the BMI of a person based on their height and weight.

    Args:
        input1 (list[int | float]): The first input
        is the height of persons in meters.
        input2 (list[int | float]): The second input
        is the weight of persons in kilograms.

    Returns:
        list[float]: The BMI of the persons.
    """
    try:
        if len(height) != len(weight):
            raise AssertionError("The length of the two lists must be the same.")
        for i in range(len(height)):
            if type(height[i]) is not int and type(height[i]) is not float:
                raise AssertionError("first list must be numbers.")
            if type(weight[i]) is not int and type(weight[i]) is not float:
                raise AssertionError("list must be numbers.")
        bmi = []
        for i in range(len(height)):
            bmi.append(weight[i] / height[i] ** 2)
        return bmi
    except Exception as e:
        print(e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    checks if bmis are conform to the limits
    """
    ret = []
    if type(limit) is not int and type(limit) is not float:
        raise AssertionError("The limit must be a number.")
    for i in range(len(bmi)):
        if type(bmi[i]) is not int and type(bmi[i]) is not float:
            raise AssertionError("The elements  must be numbers.")
        if bmi[i] < limit:
            ret.append(True)
        else:
            ret.append(False)
    return ret


def printError(e):
    """
    takes an exception and print it to the stderr formatted
    """
    print(type(e).__name__ + ": " + str(e))



def slice_me(family: list, start: int, end: int) -> list:
    """Slice the given list between the start and end indexes.

    :param family: the list to slice
    :param start: the start index
    :param end: the end index
    :return: the sliced list
    """
    try:
        length = len(family[0])
        shape = [0,0]
        for x in family:
            if(len(x)) != length:
                raise Exception('error in arrays') 
            shape[0] = shape[0] + 1

        shape[1] = len(family[0])
        print('my shape is : (' + str(shape[0]) + ',' +str(shape[1]) + ')')
        return family[start:end]
    except Exception as e:
        printError(e)



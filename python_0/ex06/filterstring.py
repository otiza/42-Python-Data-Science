import sys
from ft_filter import ft_filter


def printError(e):
    """
    takes an exception and print it to the stderr formatted
    """
    print(type(e).__name__ + ": " + str(e))


def main():
    """
    check for the number and types of arguments and call analyzeStr
    """
    if len(sys.argv) != 3:
        raise AssertionError('Bad arguments')
    if not isinstance(sys.argv[1], str):
        raise AssertionError('Bad arguments')
    try:
        int(sys.argv[2])
    except Exception:
        raise AssertionError('Bad arguments')
    args = sys.argv[1].split(" ")
    ret = list(ft_filter(lambda x: len(x) > int(sys.argv[2]), args))
    print(ret)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        printError(e)
        exit(1)

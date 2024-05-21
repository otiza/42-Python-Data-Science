import sys


def main():
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    try:
        int(sys.argv[1])
    except Exception:
        raise AssertionError("argument is not a number")
    if int(sys.argv[1]) % 2 == 0:
        print("i'm even")
    else:
        print("i'm odd")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__ + ": " + str(e))
        exit(1)

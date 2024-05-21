import sys
import re


def analyzeStr(input: str):
    """
    analyze a string and print the total of number , letters and punctuation
    """
    uppers = len(re.findall(r'[A-Z]', input))
    lowers = len(re.findall(r'[a-z]', input))
    punctuations = len(re.findall(r'[.,;:!?]', input))
    numbers = len(re.findall(r'[0-9]', input))
    spaces = len(re.findall(r' ', input))
    print("the text contains " + str(len(input)) + " characters:")
    print(str(uppers) + " upper letters")
    print(str(lowers) + " lower letters")
    print(str(punctuations) + " punctuation marks")
    print(str(spaces) + " spaces")
    print(str(numbers) + " digits")


def main():
    """check for the number of arguments and call analyzeStr"""
    if len(sys.argv) != 2:
        raise AssertionError("Too much arguments")
    else:
        analyzeStr(sys.argv[1])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__ + ": " + str(e))
        exit(1)

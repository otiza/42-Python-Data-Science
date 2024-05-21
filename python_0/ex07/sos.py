import sys
import re


def printError(e):
    """
    takes an exception and print it to the stderr formatted
    """
    print(type(e).__name__ + ": " + str(e))


MORSE_CODE_DICT = {'A': '.- ', 'B': '-... ',
                   'C': '-.-. ', 'D': '-.. ', 'E': '. ',
                   'F': '..-. ', 'G': '--. ', 'H': '.... ',
                   'I': '.. ', 'J': '.--- ', 'K': '-.- ',
                   'L': '.-.. ', 'M': '-- ', 'N': '-. ',
                   'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
                   'R': '.-. ', 'S': '... ', 'T': '- ',
                   'U': '..- ', 'V': '...- ', 'W': '.-- ',
                   'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
                   '1': '.---- ', '2': '..--- ', '3': '...-- ',
                   '4': '....- ', '5': '..... ', '6': '-.... ',
                   '7': '--... ', '8': '---.. ', '9': '----. ',
                   '0': '----- ',  ',': '--..-- ', '.': '.-.-.- ',
                   '?': '..--.. ', '/': '-..-. ', '-': '-....- ',
                   '(': '-.--. ', ')': '-.--.- ', ' ': '/ '}


def translate(msg):
    ret = ""
    for i in msg:
        if i.isalpha():
            ret += MORSE_CODE_DICT[i.upper()]
        else:
            ret += MORSE_CODE_DICT[i]
    return ret


def main():
    """
    check the arguments and call translate
    """
    if len(sys.argv) != 2:
        raise AssertionError('Bad arguments')
    if not isinstance(sys.argv[1], str):
        raise AssertionError('Bad arguments')
    if re.search("/[^A-Za-z0-9 ]/", sys.argv[1]):
        raise AssertionError('Bad arguments')
    print(translate(sys.argv[1]))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        printError(e)

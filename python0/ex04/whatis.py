import sys


def is_even(number: int) -> bool:
    if number % 2 == 0:
        print("I'm Even.")
        return True
    else :
        print("I'm Odd.")
        return False

try:
    is_even(int(sys.argv[1]))
except:
    pass
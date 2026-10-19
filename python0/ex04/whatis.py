import sys


def is_even(number: int) -> bool:
    if number % 2 == 0:
        print("I'm Even.")
        return True
    else :
        print("I'm Odd.")
        return False

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    is_even(int(sys.argv[1]))
except AssertionError as e:
    print("AssertionError:", e)
except ValueError:
    print("AssertionError: argument is not an integer")
except:
    pass
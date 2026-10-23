import sys


def main():
    """
    Handle the program's main execution.

    Retrieves a string and an integer from the command-line arguments.
    Splits the string into a list of words and filters the words according
    to their length. Prints the resulting list.

    The program expects exactly two command-line arguments: a string
    and an integer representing the minimum word length.

    Raises:
        AssertionError: If the number of command-line arguments is not two.
        ValueError: If the second argument cannot be converted to an integer.
        KeyboardInterrupt: If the user interrupts the program.
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        S: list[str] = sys.argv[1].split()
        N: int = int(sys.argv[2])

        resultat: list = [word for word in S if (lambda w: len(w) > N)]
        print(resultat)

    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")


if __name__ == "__main__":
    main()

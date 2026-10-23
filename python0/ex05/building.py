import sys


def count_characters(string: str):
    """
    Count and display the number of characters in a string.

    The function counts the total number of characters, uppercase letters,
    lowercase letters, punctuation marks, whitespace characters, and digits.
    It then prints the results to the standard output.

    Args:
        string (str): The text to analyze.

    Returns:
        None: The function prints the results and does not return a value.
    """
    total_char: int = len(string)
    upper_letters: int = 0
    lower_letters: int = 0
    punctuation_char: int = 0
    space_char: int = 0
    digit_char: int = 0

    for char in string:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1
        elif char.isdigit():
            digit_char += 1
        elif char.isspace():
            space_char += 1
        else:
            punctuation_char += 1

    print("The text contains", total_char, "characters:")
    print(upper_letters, "upper letters")
    print(lower_letters, "lower letters")
    print(punctuation_char, "punctuation marks")
    print(space_char, "spaces")
    print(digit_char, "digits")


def main():
    """
    Handle the program's main execution.

    Reads the text to analyze from a command-line argument or from
    standard input if no argument is provided. Calls count_characters()
    to display the character statistics.

    Raises:
        AssertionError: If more than one command-line argument is provided.
        KeyboardInterrupt: If the user interrupts the program.
    """

    string: str
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            string = sys.argv[1]
        else:
            print("What is the text to count?")
            string = sys.stdin.readline()
        count_characters(string)
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")


if __name__ == "__main__":
    main()

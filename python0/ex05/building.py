import sys


def count_characters(string: str):
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
    "main"

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

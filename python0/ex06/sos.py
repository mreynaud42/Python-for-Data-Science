import sys


def sos(string: str) -> str:
    """
    Convert a string into its Morse code representation.

    Converts each character of the input string into its corresponding
    Morse code sequence. Supports uppercase letters, digits, and spaces.
    Each Morse code sequence is followed by a space.

    Args:
        string (str): The text to convert. Only uppercase letters,
            digits, and spaces are supported.

    Returns:
        str: The Morse code representation of the input string.

    Raises:
        KeyError: If the string contains an unsupported character.
    """
    NESTED_MORSE: dict = {
        " ": "/ ",

        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
        'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
        'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
        'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ',

        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ',
    }
    res: str = ""

    for char in string:
        res += NESTED_MORSE[char]
    return res


def main():
    """
    Handle the program's main execution.

    Checks that exactly one command-line argument is provided,
    converts it to uppercase, translates it into Morse code using sos(),
    and prints the result without the trailing space.

    Raises:
        AssertionError: If the number of command-line arguments is not one.
        KeyError: If the input contains an unsupported character.
        KeyboardInterrupt: If the user interrupts the program.
    """

    try:
        assert len(sys.argv) == 2, "number of arguments is different from 1"
        print(sos(sys.argv[1].upper())[:-1])
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyError:
        print("AssertionError: the arguments are bad")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")


if __name__ == "__main__":
    main()

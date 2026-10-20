import sys


def sos(string: str) -> str:
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
    "main"

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

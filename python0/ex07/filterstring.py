import sys


def main():
    "main"

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

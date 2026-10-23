from ft_filter import ft_filter
from typing import Callable

CEND = '\33[0m'
CREDGB = '\33[41m'
CGREENBG = '\33[42m'


def is_fail_print(a, b) -> bool:

    if a != b:
        return 1
    return 0


def main():
    "main"

    tests: list[tuple[Callable, list]] = [
        [lambda x: x <= 1, [0, 1, 2]],
        [lambda x: x.isupper(), "AiuhIBfejrufhie90()C"],
        [lambda x: x.isdigit(), "AiuhIBfejrufhie90()C"],
        [lambda x: x**2 > 25, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        [lambda x: x**2 < 25, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        [lambda x: x**2 == 25, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        [lambda x: 0, [15.4, 84.7, 0.001]],
        [lambda x: 1, []],
        [lambda x: 1, ""],
        [None, [0, 1, 2, 0, 3, 4, 0, -1, 0]],
        [None, []],
    ]
    count_fail_test: int = 0

    if ft_filter.__doc__ != filter.__doc__:
        print(f"{CREDGB}[FAIL]{CEND}\t:")
        print(f"{filter.__doc__}")
        print()
        print(f"{ft_filter.__doc__}")
        return

    for func, values in tests:
        result_filter = list(filter(func, values))
        result_ft_filter = list(ft_filter(func, values))
        if result_filter != result_ft_filter:
            count_fail_test += 1
            print(f"{CREDGB}[FAIL]{CEND}\t:", values, func, result_filter, "!=", result_ft_filter)
        else:
            print(f"{CGREENBG}[OK]{CEND}\t:", result_filter, CEND)

    is_fail_print(list, dict)
    is_fail_print(list, list)


if __name__ == "__main__":
    main()


def slice_me(family: list, start: int, end: int) -> list:
    ""
    try:
        assert isinstance(family, list), "family must be lists"
        assert isinstance(start, int), "start must be int"
        assert isinstance(end, int), "end must be int"
        assert len(family) != 0, "family must contain at least one element"

        result: list = family[start:end]
        assert len(result) != 0, "result contains no elements"
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print(f"My new shape is : ({len(result)}, {len(result[0])})")

        return result

    except AssertionError as e:
        print("AssertionError: slice_me:", e)
    except TypeError as e:
        print("TypeError: slice_me:", e)

    return []


def main():
    "main of tests"
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()

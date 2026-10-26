
def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate the BMI for each pair of height and weight."""
    try:
        assert isinstance(height, list), "height must be lists"
        assert isinstance(weight, list), "weight must be lists"
        assert len(height) == len(weight), "height and weight must have the same length"

        bmi_list: list[int | float] = []

        for h, w in zip(height, weight):
            assert isinstance(h, (int, float)), "height must contain only numbers"
            assert isinstance(w, (int, float)), "weight must contain only numbers"
            assert h == h and w == w, "height and weight must be a numbers"
            assert h != float("inf") and w != float("inf"), "height and weight must not be infinite"
            assert h > 0 and w > 0, "height and weight must be positive"

            bmi_list.append(w/h**2)

        return bmi_list

    except AssertionError as e:
        print("AssertionError: give_bmi:", e)

    return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value greater than the specified limit."""
    try:
        assert isinstance(bmi, list), "bmi must be lists"
        assert isinstance(limit, int), "limit must be int"
        assert limit >= 0, "limit must not be negative"

        bmi_limit: list[bool] = list(map(lambda v: v > limit, bmi))

        return bmi_limit

    except AssertionError as e:
        print("AssertionError: apply_limit:", e)
    except TypeError as e:
        print("TypeError: apply_limit:", e)

    return []


def main():
    "main of tests"
    tests: list[tuple[list[int | float], list[int | float], int]] = [
        [[2.71, 1.15], [165.3, 38.4], 26],
        [[2], [1], 26],
        [[2.7], [6], 26],
        [[2.71], [165.3, 38.4], 26],
        [["2.71"], [165.3], 26],
        [[[]], [165.3], 26],
        [5, [165.3], 26],
        [[-2], [-1.3], 26],
        [[0], [0], 26],
        [[1], [float("nan")], 10],
        [[float("nan")], [1], 10],
        [[float("nan")], [float("nan")], 10],
        [[1], [float("inf")], 10],
        [[float("inf")], [1], 10],
        [[float("inf")], [float("inf")], 10],
        [[], [], 0],
        [[2.71, 1.15], [165.3, 38.4], -26],
        [[2.71, 1.15], [165.3, 38.4], 0],
        [[2], [1], 22.],
        [[2], [1], {}],
        [[2], [True], True],
    ]

    for height, weight, limit in tests:
        bmi = give_bmi(height, weight)
        print(height, weight, "=>", bmi)
        print(limit, "=>", apply_limit(bmi, limit))
        print()


if __name__ == "__main__":
    main()

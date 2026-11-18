
from pandas import DataFrame, read_csv


def load(path: str) -> DataFrame:
    ""
    try:
        assert isinstance(path, str), "path must be str"

        data =read_csv(path)
    except (
        AssertionError, FileNotFoundError,
        PermissionError, IsADirectoryError,
    ) as e:
        print(f"{type(e).__name__}: load: {e}")
        return None

    return data


def main():
    "main of tests"
    print(load("../data/life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
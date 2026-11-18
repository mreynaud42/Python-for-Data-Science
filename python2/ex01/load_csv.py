
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
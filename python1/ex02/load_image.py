from PIL import Image, UnidentifiedImageError
from PIL.Image import DecompressionBombError
import warnings
import numpy as np
from numpy.typing import NDArray


def ft_load(path: str) -> NDArray[np.uint8] | None:
    ""
    try:
        assert isinstance(path, str), "path must be str"

        warnings.simplefilter('error', Image.DecompressionBombWarning)
        img: Image.Image = Image.open(path)
        array: NDArray[np.uint8] = np.array(img)

        print("The shape of image is:", array.shape)

        return array

    except (
        AssertionError,
        FileNotFoundError,
        UnidentifiedImageError,
        IsADirectoryError,
        DecompressionBombError
    ) as e:
        print(f"{type(e).__name__}: ft_load: {e}")

    return None


def main():
    "main of tests"
    tests: list[str] = [
        "landscape.jpg",
        "animal.jpeg",
        "load_image.py",
        "no_file",
        "no_access",
        "..",
        {},
    ]

    for t in tests:
        print(ft_load(t))
        print("-" * 50)
        print()


if __name__ == "__main__":
    main()

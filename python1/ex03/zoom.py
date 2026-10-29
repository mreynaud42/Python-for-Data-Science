from PIL import UnidentifiedImageError
from PIL.Image import DecompressionBombError
import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
from load_image import ft_load


def ft_zoom(path: str) -> None:
    ""
    try:
        array: NDArray[np.uint8] = ft_load(path)
    except (
        AssertionError, FileNotFoundError,
        PermissionError, IsADirectoryError,
        UnidentifiedImageError, DecompressionBombError
    ) as e:
        print(f"{type(e).__name__}: ft_load: {e}")
        return None

    print(array)

    height: int = array.shape[0]
    height = (height + 400) // 2 if height > 400 else 400
    width: int = array.shape[1]
    width = (width + 400) // 2 if width > 400 else 400
    array = array[height - 400:height, width - 400:width, 0]

    print(
        "New shape after slicing: "
        f"{array[:, :, np.newaxis].shape} or {array.shape}"
    )
    print(array)

    try:
        plt.imshow(array, cmap="gray")
        plt.show()
    except (TypeError, IndexError, OSError, MemoryError) as e:
        print(f"{type(e).__name__}: ft_zoom: {e}")
        return None


def main():
    "main of tests"
    ft_zoom("../image/animal.jpeg")
    ft_zoom("../image/landscape.jpg")


if __name__ == "__main__":
    main()

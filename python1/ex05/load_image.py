from PIL import Image, UnidentifiedImageError
from PIL.Image import DecompressionBombError
import matplotlib.pyplot as plt
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
    except (
        AssertionError, FileNotFoundError,
        PermissionError, IsADirectoryError,
        UnidentifiedImageError, DecompressionBombError
    ) as e:
        print(f"{type(e).__name__}: ft_load: {e}")
        return None

    print(f"The shape of image is: {array.shape}")
    print(array)

    return array


def ft_show(array_img: NDArray[np.uint8]) -> None:
    ""
    try:
        plt.imshow(array_img)
        plt.show()
    except (TypeError, IndexError, OSError, MemoryError) as e:
        print(f"{type(e).__name__}: ft_show: {e}")
        return None

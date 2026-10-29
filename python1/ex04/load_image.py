from PIL import Image, UnidentifiedImageError
from PIL.Image import DecompressionBombError
import matplotlib.pyplot as plt
import warnings
import numpy as np
from numpy.typing import NDArray


def ft_load(path: str) -> NDArray[np.uint8]:
    ""
    assert isinstance(path, str), "path must be str"

    warnings.simplefilter('error', Image.DecompressionBombWarning)
    img: Image.Image = Image.open(path)
    array: NDArray[np.uint8] = np.array(img)

    return array


def ft_cut_square(path: str) -> NDArray[np.uint8] | None:
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

    height: int = (array.shape[0] + 400) // 2
    width: int = (array.shape[1] + 400) // 2
    if height < 400 or width < 400:
        height = width = min(array.shape[0], array.shape[1])
        array = array[:height, :width, 0]
    else:
        array = array[height - 400:height, width - 400:width, 0]

    print(
        "The shape of image is: "
        f"{array[:, :, np.newaxis].shape} or {array.shape}"
    )
    print(array)

    return array


def ft_show(array_img: NDArray[np.uint8]) -> None:
    ""
    try:
        plt.imshow(array_img, cmap="gray")
        plt.show()
    except (TypeError, IndexError, OSError, MemoryError) as e:
        print(f"{type(e).__name__}: ft_show: {e}")
        return None

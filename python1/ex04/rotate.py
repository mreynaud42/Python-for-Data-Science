import numpy as np
from numpy.typing import NDArray
from load_image import ft_cut_square, ft_show


def rotate(path: str) -> NDArray[np.uint8] | None:
    ""
    array: NDArray[np.uint8] = ft_cut_square(path)
    if array is None:
        return None

    array = array.T

    print(f"New shape after Transpose: {array.shape}")
    print(array)

    return array


def main():
    "main of tests"
    array1: NDArray[np.uint8] = rotate("../image/animal.jpeg")
    if array1 is not None:
        ft_show(array1)
    array2: NDArray[np.uint8] = rotate("../image/landscape.jpg")
    if array2 is not None:
        ft_show(array2)


if __name__ == "__main__":
    main()

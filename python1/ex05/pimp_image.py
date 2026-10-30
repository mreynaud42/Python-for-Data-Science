from numpy.typing import NDArray
import numpy as np
from load_image import ft_load, ft_show


def ft_invert(array: NDArray) -> NDArray:
    "Inverts the color of the image received."
    return 255 - array


def ft_red(array: NDArray) -> NDArray:
    "Keeps only the red channel of the image received."
    return [1, 0, 0] * array


def ft_green(array: NDArray) -> NDArray:
    "Keeps only the green channel of the image received."
    array[:, :, 0] -= array[:, :, 0]
    array[:, :, 2] -= array[:, :, 2]
    return array


def ft_blue(array: NDArray) -> NDArray:
    "Keeps only the blue channel of the image received."
    array[:, :, 0:2] = 0
    return array


def ft_grey(array: NDArray) -> NDArray:
    "Converts an RGB image to grayscale using the green channel."
    array[:, :, 0] = array[:, :, 2] = array[:, :, 1]
    return array


def main():
    "main of tests"
    img_array: NDArray = ft_load("../image/landscape.jpg")
    if img_array is None:
        return

    img_invert_array: NDArray = ft_invert(img_array.copy())
    img_red_array: NDArray = ft_red(img_array.copy())
    img_green_array: NDArray = ft_green(img_array.copy())
    img_blue_array: NDArray = ft_blue(img_array.copy())
    img_grey_array: NDArray = ft_grey(img_array.copy())

    try:
        ft_show(img_array)
        ft_show(img_invert_array)
        ft_show(img_red_array)
        ft_show(img_green_array)
        ft_show(img_blue_array)
        ft_show(img_grey_array)
    except KeyboardInterrupt as e:
        print(f"{type(e).__name__}")


if __name__ == "__main__":
    main()

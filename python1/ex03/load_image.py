from PIL import Image
import warnings
import numpy as np
from numpy.typing import NDArray


def ft_load(path: str) -> NDArray[np.uint8]:
    ""
    assert isinstance(path, str), "path must be str"

    warnings.simplefilter('error', Image.DecompressionBombWarning)
    img: Image.Image = Image.open(path)
    array: NDArray[np.uint8] = np.array(img)

    print("The shape of image is:", array.shape)

    return array

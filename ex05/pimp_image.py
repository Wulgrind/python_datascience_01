import numpy as np
import matplotlib.pyplot as plt


def display(array: np.ndarray) -> np.ndarray:
    plt.imshow(array)
    plt.axis("off")
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
Inverts the color of the image received.
    """
    invert = 255 - array
    display(invert)
    return invert


def ft_red(array: np.ndarray) -> np.ndarray:
    """
Turn to red the colors of the image received.
    """
    result = np.zeros_like(array)
    result[..., 0] = array[..., 0] * 1
    display(result)
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """
Turn to green the colors of the image received.
    """
    result = np.zeros_like(array)
    result[..., 1] = array[..., 1] - 0
    display(result)
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
Turn to blue the colors of the image received.
    """
    result = np.zeros_like(array)
    result[..., 2] = array[..., 2]
    display(result)
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
Turn to grey the colors of the image received.
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    display(grey_image.astype(np.uint8))
    return grey_image

import numpy as np


def center_crop(img: np.array, new_width: int = None, new_height: int = None):
    """
    Crops an image to fit a circle

    :param img: numpy.array object
    :param new_width: int with new width of a picture
    :param new_height: int with new height of a picture
    :return: numpy.array object with cropped image
    """

    width = img.shape[1]
    height = img.shape[0]

    if new_width is None:
        new_width = min(width, height)

    if new_height is None:
        new_height = min(width, height)

    left = int(np.ceil((width - new_width) / 2))
    right = width - int(np.floor((width - new_width) / 2))

    top = int(np.ceil((height - new_height) / 2))
    bottom = height - int(np.floor((height - new_height) / 2))

    if len(img.shape) == 2:
        center_cropped_img = img[top:bottom, left:right]
    else:
        center_cropped_img = img[top:bottom, left:right, ...]

    return center_cropped_img

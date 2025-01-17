import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def rotate_img(path: str):
    img_array = ft_load(path)
    transposed_img_array = np.empty((len(img_array), len(img_array)))
    i = 0
    while i < len(img_array):
        j = 0
        while j < len(img_array):
            transposed_img_array[i, j] = img_array[j, i].item()
            j += 1
        i += 1
    print("New shape after Transpose: (400, 400)")
    print(transposed_img_array)
    plt.imshow(transposed_img_array, cmap='gray')
    plt.show()


if __name__ == '__main__':
    rotate_img('animal.jpeg')

import numpy as np
import matplotlib.pyplot as plt


def rotate_img(img_array: np.ndarray):
    transposed_img_array = np.transpose(img_array.squeeze(), (1, 0))
    print("New shape after Transpose: (400, 400)")
    print(transposed_img_array)
    plt.imshow(transposed_img_array, cmap='gray')
    plt.title("Transposed Image (Rotated 90° Left)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

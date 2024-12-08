from PIL import Image
import numpy as np
from rotate import rotate_img


def ft_load(path: str) -> np.ndarray:
    try:
        with Image.open(path) as img:
            img_format = img.format
            if img_format not in ['JPEG', 'JPG']:
                raise ValueError(
                    "Only JPG/JPEG are supported as images. Verify your args.")
            img = img.convert('RGB')
            img_array = np.array(img)
            crop_size = 400
            height, width, channels = img_array.shape
            center_x, center_y = width // 2 + 130, height // 2 - 90
            crpd_img_a = img_array[
                center_y - crop_size // 2:center_y + crop_size // 2,
                center_x - crop_size // 2:center_x + crop_size // 2,
                :
            ]
            if channels > 1:
                crpd_img_a = crpd_img_a[..., :1]
            print(
                f"The shape of the image is: {crpd_img_a.shape} or (400, 400)")
            print(crpd_img_a)
            rotate_img(crpd_img_a)
            return img_array

    except Exception as e:
        print((f"Error: {e}"))


if __name__ == '__main__':
    ft_load('animal.jpeg')

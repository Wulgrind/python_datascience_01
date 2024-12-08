from PIL import Image
import numpy as np
from zoom import zoom_img


def ft_load(path: str) -> np.ndarray:
    """
Load images
    """
    try:
        with Image.open(path) as img:
            img_format = img.format
            if img_format not in ['JPEG', 'JPG']:
                raise ValueError(
                    "Only JPG/JPEG are supported as images. Verify your args.")
            img = img.convert('RGB')
            img_array = np.array(img)
            print(f"The shape of the image is: {img_array.shape}")
            print(img_array)
            zoom_img(img_array)
            return img_array
    except Exception as e:
        print((f"Error: {e}"))


if __name__ == '__main__':
    ft_load('animal.jpeg')

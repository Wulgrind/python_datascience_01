from PIL import Image
import numpy as np


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
            return img_array
    except Exception as e:
        print((f"Error: {e}"))

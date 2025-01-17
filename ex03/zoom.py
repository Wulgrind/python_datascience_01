import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_img(path: str):
    """
Zoom on images
    """
    img_array = ft_load(path)
    crop_size = 400
    height, width, channels = img_array.shape
    center_x, center_y = width // 2 + 130, height // 2 - 90
    cropped_img_array = img_array[
        center_y - crop_size // 2:center_y + crop_size // 2,
        center_x - crop_size // 2:center_x + crop_size // 2,
        :
    ]
    if channels > 1:
        cropped_img_array = cropped_img_array[..., :1]
    print(f"New shape after slicing: {cropped_img_array.shape} or (400, 400)")
    print(cropped_img_array)
    plt.figure(figsize=(8, 8))
    plt.imshow(cropped_img_array.squeeze(),
               cmap='gray', interpolation='nearest')
    plt.xlabel('X-axis (pixels)')
    plt.ylabel('Y-axis (pixels)')
    plt.title('Zoomed Image')
    plt.show()


if __name__ == '__main__':
    zoom_img('animal.jpeg')

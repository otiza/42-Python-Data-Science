from load_image import load_image
import cv2 as cv2
from PIL import Image
from zoom import ft_zoom
import numpy as np

def rotate_image(image):

    height = image.shape[0]
    width = image.shape[1]
    rotated_image = []
    for j in range(width):
        new_row = []
        for i in range(height - 1, -1, -1):
            new_row.append(image[i][j])
        rotated_image.append(new_row)

    return rotated_image


img = load_image('animal.jpeg')
img = ft_zoom(img)
rot = np.array( rotate_image(img))

cv2.imshow('rotated image',rot)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2 as cv2
from load_image import load_image

def ft_zoom(image_array):
    (x, y, z) = image_array.shape

    xoff = int(x / 2)
    yoff = int(y / 2)
    if xoff < 400:
        xoff = 400
    cropped_image = image_array[xoff - 400:xoff, yoff:yoff+400, 0:1]

    print(cropped_image.shape)

    cv2.imshow('test', image_array)
    cv2.imshow('Zoomed Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imag = load_image('./animal.jpeg')
ft_zoom(imag)

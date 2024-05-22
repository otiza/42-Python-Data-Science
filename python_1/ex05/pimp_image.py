import numpy as np
from load_image import load_image
import cv2 as cv2

def ft_invert(image):
    for x in image:
        for pxl in x:
           pxl[0] = 255 - pxl[0]
           pxl[1] = 255 - pxl[1]
           pxl[2] = 255 - pxl[2]
    return image

def ft_red(image):
    for x in image:
        for pxl in x:
           pxl[0] = 0
           pxl[1] = 0
    return image

def ft_green(image):
    for x in image:
        for pxl in x:
           pxl[0] = 0
           pxl[2] = 0
    return image


def ft_blue(image):
    for x in image:
        for pxl in x:
           pxl[1] = 0
           pxl[2] = 0
    return image

def ft_grey(image):
    for x in image:
        for pxl in x:
           avg  = np.mean(pxl).astype(int)
           pxl[0] = avg
           pxl[1] = avg
           pxl[2] = avg
    return image


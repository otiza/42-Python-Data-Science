from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green,ft_blue, ft_grey
array = ft_load("p.jpeg")
import cv2 as cv2
cv2.imshow('Original Image', array)
ft_invert(array)
cv2.imshow('Inverted Image', ft_invert(array))

ft_red(array)
cv2.imshow('Red Image', ft_red(array))
ft_green(array)
cv2.imshow('Green Image', ft_green(array))

ft_blue(array)
cv2.imshow('Blue Image', ft_blue(array))
ft_grey(array)
cv2.imshow('Grey Image', ft_grey(array))
print(ft_invert.__doc__)
cv2.waitKey(0)
cv2.destroyAllWindows()
from matplotlib import image
from matplotlib import pyplot

def ft_load(path):
    #try:
        img = image.imread(path)
        print("the shape of the image is : "+ str(img.shape))
        print(img)
        return img
    #except:
     #   print('image not able to be loaded')

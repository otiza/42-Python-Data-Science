from matplotlib import image
from matplotlib import pyplot

def load_image(path):
    try:
        image = image.imread(path)
        pyplot.imshow(image)
        print("the shape of the image is : "+ str(image.shape))
        print(image)
    except:
        print('image not able to be loaded')

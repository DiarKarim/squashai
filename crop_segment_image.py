# Importing Image class from PIL module
from PIL import Image
import os 
from rembg import remove 

path = "RawImages/"
path2save = "CroppedImages/"

files = os.listdir(path)

for file in files: 

    # Opens a image in RGB mode
    im = Image.open(path + file)

    # Setting the points for cropped image
    left = 0
    top = 500
    right = 960
    bottom = 1750
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    # Removing the background from the given Image (segment image) 
    output = remove(im1) 

    output.save(path2save + "cs_" + file)
    
im1.show()
# Importing Image class from PIL module
from PIL import Image
import os 
from rembg import remove 

path = "RawImages/Stuart Take 2 Raw/"
path2save = "CroppedImages/Stuart Take 2 Cropped and Segmented/"

files = os.listdir(path)

# For testing only look at 5 files 
# files = files[0:5]

counter = 0
for file in files: 

    # Opens a image in RGB mode
    im = Image.open(path + file)

    # Setting the points for cropped image
    left = 0
    top = 0
    right = 960
    bottom = 1350
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    # Removing the background from the given Image (segment image) 
    output = remove(im1) 

    output.save(path2save + "cs_" + file)

    counter = counter + 1
    print(str(counter) + " / " + str(len(files)))

im1.show()
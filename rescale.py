import os
from scipy import ndimage, misc
import scipy.misc
import re,glob
test_imgs = glob.glob("test_stg1/*.jpg")


images = []
for root, dirnames, filenames in os.walk("test_stg1/"):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            filepath = os.path.join(root, filename)
            image = ndimage.imread(filepath, mode="RGB")
            image_resized = misc.imresize(image, (480,640))
            scipy.misc.toimage(image_resized).save('test_stg1/rescaled/%s_resized.jpg' %(filename))

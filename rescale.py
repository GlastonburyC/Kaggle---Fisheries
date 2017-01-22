import os
from scipy import ndimage, misc
import scipy.misc
import re,glob
import cv2
test_imgs = glob.glob("test_stg1/*.jpg")

for filename in test_imgs:
    image = ndimage.imread(filename, mode="RGB")
    image_resized = misc.imresize(image, (480,640))
    out_file=filename.split('.')[0].split('/')[1]
    scipy.misc.toimage(image_resized).save('test_stg1/rescaled/%s_resized.jpg' %(out_file))


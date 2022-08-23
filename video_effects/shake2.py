from audioop import mul
from email.mime import image
from importlib.resources import path
import cv2 as cv
import os,sys
import numpy as np
from random import *
import matplotlib.image as mpimg
import time

pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
print('image_path: '+image_path+' pathname: '+pathname)
img = cv.imread(image_path)

kernel_size = 1


height, width  = img.shape[:2]

timestr = time.strftime("%Y-%m-%d %H-%Mm-%Ss")
print(timestr)
#Caracteristicas del video
out = cv.VideoWriter(pathname+'/shake '+timestr+'.wmv',cv.VideoWriter_fourcc(*'mp4v'),60,(width,height))

for i in range(1,100):
    multi = kernel_size * randint(1,100)
    kernel_v = np.zeros((multi, multi), dtype=np.float64)
    kernel_v[:, int((multi - 1)/2)] = np.ones(multi)
    kernel_v /= multi
    vertical_mb = cv.filter2D(img, -1, kernel_v)
    out.write(vertical_mb)
out.release()
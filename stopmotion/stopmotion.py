import cv2 as cv
import os,sys
import numpy as np
import glob

img_array = []

for filename in glob.glob("C:/Users/vx/Pictures/drive-download-20220301T202852Z-001/*.JPG"):
    img = cv.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
#3 = FPS
out = cv.VideoWriter('project.avi',cv.VideoWriter_fourcc(*'DIVX'), 3, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
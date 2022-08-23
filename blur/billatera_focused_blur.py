import cv2 as cv
import numpy as np
import os,sys
#Gaussian bilateral está más cerca del efecto microdermoabrasión
def bi_demo(img):
    #dst = cv2.bilateralFilter (src, depht, sigmaColor, sigmaSpace [, dst [, borderType]])
    dst = cv.bilateralFilter(img, 3, 20, 15)
    cv.imshow("bi_demo", dst)

pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = cv.imread(image_path)


cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", img)
bi_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()

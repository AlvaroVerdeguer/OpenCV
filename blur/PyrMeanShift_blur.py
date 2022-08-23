import cv2 as cv
import numpy as np
import os,sys
#均值迁移 可能会过度模糊，有种油画的效果
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("bi_demo", dst)

pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = cv.imread(image_path)


cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", img)
shift_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()

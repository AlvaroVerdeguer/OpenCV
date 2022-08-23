import cv2 as cv
import os,sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg



pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = cv.imread(image_path)


multi = 30
kernel_v = np.zeros((multi, multi), dtype=np.float64)
kernel_v[:, int((multi - 1)/2)] = np.ones(multi)
kernel_v /= multi
vertical_mb = cv.filter2D(img, -1, kernel_v)


cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", vertical_mb)
cv.waitKey(0)
cv.destroyAllWindows()




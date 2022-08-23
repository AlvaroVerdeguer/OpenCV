import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os
import sys

pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = cv.imread(image_path)
img = mpimg.imread(image_path)
kernel_size = 30

kernel_h = np.zeros((kernel_size, kernel_size))

kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)

kernel_h /= kernel_size

horizonal_mb = cv.filter2D(img, -1, kernel_h)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.axis("off")

plt.subplot(122),plt.imshow(horizonal_mb),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

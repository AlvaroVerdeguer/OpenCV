import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
import matplotlib.image as mpimg


print( cv.__version__ )
# !variables
pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = cv.imread(image_path)
img = mpimg.imread(image_path)

# !blur_intesity
billateral = cv.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(billateral),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()




#! Aquí, la función cv.medianBlur() toma la mediana de todos los píxeles debajo del área del kernel
#! y el elemento central se reemplaza con este valor mediano.
#! Esto es muy efectivo contra el ruido de sal y pimienta en una imagen.
#! Su tamaño de kernel debe ser un entero impar positivo.
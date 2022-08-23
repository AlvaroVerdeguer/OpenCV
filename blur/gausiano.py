import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import sys
import os


print( cv.__version__ )
# !variables
pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = mpimg.imread(image_path)


# !blur_intesity
blur = cv.GaussianBlur(img,(1,41),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()




# ! Como parámetros de entrada se tienen que pasar el ancho y la altura del kernel, que debe ser positivo y impar.
# ! Además hay que especificar la desviación estándar en las direcciones X e Y, sigmaX y sigmaY, respectivamente. 
# ! Este tipo de filtrado es muy eficaz para eliminar el ruido gaussiano de la imagen.
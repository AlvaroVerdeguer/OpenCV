import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
import matplotlib.image as mpimg

# !explicacion del blur por promedio
#creas una capa a la cual les das unas dimensiones, 5 de alto por 5 de ancho
#esa capa se superpone a la imagen original y suma todos los valores de la capa( el valor maximo posible es 1)
#divideo la suma de todos los valores entre la cantidad de pixeles de la capa, en este caso 25
#aplica el promedio como valor al pixel al cual se le habia aplicado el filtro

print( cv.__version__ )
# !variables
pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = mpimg.imread(image_path)


# !blur_intesity
bi= int(input('intensidad del difuminado: '))
kernel = np.ones((bi,bi),np.float32)/(bi*bi)
print(kernel)

dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()






#! blur gausiano

	
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

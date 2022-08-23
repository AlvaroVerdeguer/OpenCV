import cv2 as cv
import numpy as np
import os, sys
from matplotlib import pyplot as plt

#función truncada
def clamp(pv):
    if pv > 255:
        return 255
    else:
        return pv

intensidad_color=0
cantidad_granulado=30
size = 5
#filtro gaussiano
def gaussian_noise(image):
    #rows,columns,channels
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(intensidad_color, cantidad_granulado,size)#0 es la media de todos los números aleatorios en la matriz, 20 es la desviación estándar, 3 es la forma (1 fila y 3 columnas)
            b = image[row, col, 0] #blue (saca el canal azul de el pixel de la fila row y columna col)
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[0])
            image[row, col, 2] = clamp(r + s[0])
    cv.imshow("gaussian_noise", image)


pathname = os.path.dirname(sys.argv[0])
image_path=os.path.dirname(pathname)+"/img/gato.jpg"
img = cv.imread(image_path)

cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", img)
t1 = cv.getTickCount()
gaussian_noise(img)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print(time)

cv.waitKey(0)
cv.destroyAllWindows()

# ! Parameters of Numpy Random normal()

    #!loc: It is an optional parameter. Input is like an array-like or a float value. It specifies the mean of the distribution. By default, it is 0.0.
    #!scale: It is an optional parameter. Input is like an array-like or a float value. It specifies the standard deviation or the flatness of the distribution graph should like. By default, it is 1.0. It must not be a negative value.
    #!size: It is an optional parameter. Input is like an integer or a tuple of integer. It specifies the shape of the resultant array. If the size is None. By default, it is 1.
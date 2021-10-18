# Implementar la dilatación y erosión de una imagen a escala de grises

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from scipy import ndimage


def imageToArray(filename:str, rgb:bool=False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array


A = imageToArray("imagenes/imagen11.jpg")

A_dilatada =ndimage.grey_dilation(A,3);
A_erosionada =ndimage.grey_erosion(A,3);


# Imagen A
plt.subplot(1, 3, 1)
plt.title('Imagen A')
plt.imshow(A, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Dilatada')
plt.imshow(A_dilatada, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Erosionada')
plt.imshow(A_erosionada, cmap='gray')


plt.show()
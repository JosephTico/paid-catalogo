# Implementar la apertura y clausura de una imagen a escala de grises



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

A_apertura =ndimage.grey_closing(A,3);
A_clausura =ndimage.grey_erosion(A,3);


# Imagen A
plt.subplot(1, 3, 1)
plt.title('Imagen A')
plt.imshow(A, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Apertura')
plt.imshow(A_apertura, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Clausura')
plt.imshow(A_clausura, cmap='gray')


plt.show()
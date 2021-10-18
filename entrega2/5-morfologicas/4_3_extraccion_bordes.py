# Obtener los bordes de una imagen binaria

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

def binaria(input_image, th=127):
    result_image=input_image>=127
    return result_image

def borde(input_image, structure_rank=2, structure_connectivity=1):
    structure=ndimage.generate_binary_structure(structure_rank, structure_connectivity)
    result_image = ndimage.binary_erosion(input_image,structure=structure )
    result_image = input_image & ~result_image
    return result_image

A = imageToArray("imagenes/imagen6.jpg")
A_bin = binaria(A)

A_borde =borde(A_bin)


# Imagen A
plt.subplot(1, 3, 1)
plt.title('Imagen A')
plt.imshow(A_bin, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Bordes')
plt.imshow(A_borde, cmap='gray')


plt.show()
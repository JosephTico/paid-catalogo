# Rellenar un circulo en una imagen binaria


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

def rellenar(input_image, structure_rank=2, structure_connectivity=1, max_iterations=200):
    structure=ndimage.generate_binary_structure(structure_rank, structure_connectivity)
    result_image = np.zeros(input_image.shape)
    m,n = input_image.shape
    result_image[(m+1)//2,(n+1)//2] = True
    for y in range(max_iterations):
        result_image = ndimage.binary_dilation(result_image,structure=structure)
        result_image = result_image & ~input_image
    return result_image

A = imageToArray("imagenes/imagen7.jpg")
A_bin = binaria(A)

A_rellena =rellenar(A_bin)


# Imagen A
plt.subplot(1, 3, 1)
plt.title('Imagen A')
plt.imshow(A_bin, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Rellena')
plt.imshow(A_rellena, cmap='gray')


plt.show()
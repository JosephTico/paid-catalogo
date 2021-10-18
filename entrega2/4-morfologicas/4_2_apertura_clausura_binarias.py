# Implementar la apertura y clausura de una imagen binaria

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

def apertura(input_image,structure_rank=2, structure_connectivity=1):
    structure=ndimage.generate_binary_structure(structure_rank, structure_connectivity)
    result_image = ndimage.binary_erosion(input_image,structure=structure )
    result_image = ndimage.binary_dilation(result_image,structure=structure )
    return result_image

def clausura(input_image, structure_rank=2, structure_connectivity=1):
    structure=ndimage.generate_binary_structure(structure_rank, structure_connectivity)
    result_image = ndimage.binary_dilation(input_image,structure=structure )
    result_image = ndimage.binary_erosion(result_image,structure=structure )
    return result_image



A = imageToArray("imagenes/imagen5.jpg")
A_bin = binaria(A)

# A_dilatada = ndimage.binary_dilation(A_bin, structure=np.ones((3,3)))
# A_dilatada = ndimage.binary_dilation(A_bin, structure=np.ones((2,2)))
# A_dilatada = ndimage.binary_dilation(A_bin)
# A_erosionada = ndimage.binary_dilation(A_bin)

A_apertura=apertura(A_bin, 2)



A_clausura=clausura(A_bin, 2)


# Imagen A
plt.subplot(1, 3, 1)
plt.title('Imagen A')
plt.imshow(A_bin, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Apertura')
plt.imshow(A_apertura, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Clausura')
plt.imshow(A_clausura, cmap='gray')

plt.show()

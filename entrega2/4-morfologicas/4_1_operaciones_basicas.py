# Implementar el complemento, unión, intersección y diferencia de imágenes binarias

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def imageToArray(filename:str, rgb:bool=False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array

def binaria(input_image, th=127):
    result_image=input_image>=127
    return result_image


A = imageToArray("imagenes/imagen3.jpg")
A_bin = binaria(A)

B = imageToArray("imagenes/imagen2.jpg")
B_bin = binaria(B)

A_complemento = A_bin==0

Union_A_B = A_bin | B_bin
Interseccion_A_B = A_bin & B_bin
Diferencia_A_B = A_bin != B_bin




# Imagen A
plt.subplot(2, 3, 1)
plt.title('Imagen A')
plt.imshow(A_bin, cmap='gray')

# Imagen B
plt.subplot(2, 3, 4)
plt.title('Imagen B')
plt.imshow(B_bin, cmap='gray')

# # Complemento A
plt.subplot(2, 3, 2)
plt.title('Complemento A')
plt.imshow(A_complemento, cmap='gray')

# # Union A y B
plt.subplot(2, 3, 3)
plt.title('Union A y B')
plt.imshow(Union_A_B, cmap='gray')

# # Interseccion A y B
plt.subplot(2, 3, 5)
plt.title('Interseccion A y B')
plt.imshow(Interseccion_A_B, cmap='gray')

# # Diferencia A y B
plt.subplot(2, 3, 6)
plt.title('Diferencia A y B')
plt.imshow(Diferencia_A_B, cmap='gray')

plt.show()

# Filtro Gaussiano (Rechazo de Banda)
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from scipy import ndimage


def imageToArray(filename: str, rgb: bool = False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array


img = imageToArray("camarografo.jpg")
ruido = imageToArray("ruido_periodico.jpg")

A = (img*(3/4)+ruido*(1/4)).astype(float)

F1 = np.fft.fft2(A)
D1 = np.fft.fftshift(F1)
freq_base = np.log(1+np.abs(D1))


m, n = A.shape
dist = np.zeros(A.shape)
m1 = m//2
n1 = n//2
for i in range(m):
    for j in range(n):
        dist[i, j] = np.sqrt((i-m1)**2 + (j-n1)**2)

W = 6
D0 = 32
H = np.ones(A.shape)
# ind = ((D0-W/2) <= dist) & (dist <= (D0+W/2))
H = 1 - np.exp((-1/2)*((dist**2-D0**2)/(dist*W))**2)

F2 = np.fft.fftshift(H)*F1
D2 = np.fft.fftshift(F2)
freq_filtrada = np.log(1+np.abs(D2))


A_filtrada = np.fft.ifft2(F2)
A_filtrada = np.real(A_filtrada)

plt.subplot(2, 3, 1)
plt.title('Imagen A')
plt.imshow(A, cmap='gray')

plt.subplot(2, 3, 4)
plt.title('Frecuencia imagen')
plt.imshow(freq_base, cmap='gray')


plt.subplot(2, 3, 2)
plt.title('Filtro rechaza banda Gaussiano')
plt.imshow(H, cmap='gray')

plt.subplot(2, 3, 5)
plt.title('Frecuencia imagen con filtro')
plt.imshow(freq_filtrada, cmap='gray')


plt.subplot(2, 3, 3)
plt.title('Imagen con filtro')
plt.imshow(A_filtrada, cmap='gray')


plt.show()

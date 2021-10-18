import numpy as np
from skimage import io
from skimage.color import rgb2gray
from scipy import ndimage, misc
import matplotlib.pyplot as plt

# Configurar matplotlib
plt.gray()

# Cargar imagen
image = io.imread('chest.jpg')

# Calcular DFT-2D
fft = np.fft.fft2(rgb2gray(image))

# Convolucionar con el filtro gaussiano
sigma = 2
freq_result = ndimage.fourier_gaussian(fft, sigma=sigma)

# FFT inverso
img_result = np.fft.ifft2(freq_result)


# Mostrar imagen
plt.subplot(2, 2, 1)
plt.title('Imagen')
plt.imshow(image, cmap='gray')

# Mostrar DFT-2D
plt.subplot(2, 2, 2)
plt.title('DFT-2D (shift)')
plt.imshow(np.log(1 + np.abs(np.fft.fftshift(fft))), cmap='gray')

# Mostrar filtro aplicado
plt.subplot(2, 2, 3)
plt.title('Filtro aplicado')
plt.imshow(np.log(1 + np.abs(np.fft.fftshift(freq_result))), cmap='gray')

# Imagen filtrada
plt.subplot(2, 2, 4)
plt.title('Imagen reconstruida')
plt.imshow(img_result.real)

plt.show()

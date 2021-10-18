import numpy as np
from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Cargar imagen
image = io.imread('chest.jpg')

fft = np.fft.fftshift(np.fft.fft2(rgb2gray(image)))

# Mostrar imagen
plt.subplot(2, 1, 1)
plt.title('Imagen')
plt.imshow(image, cmap='gray', vmin=0, vmax=255)

# Mostrar DFT-2D
plt.subplot(2, 1, 2)
plt.title('DFT-2D (shift)')
plt.imshow(np.log(1 + np.abs(fft)), cmap='gray')


plt.show()

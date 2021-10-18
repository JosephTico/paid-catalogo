import numpy as np
from skimage import io
from skimage.color import rgb2gray
from scipy.spatial import distance
import matplotlib.pyplot as plt

# Configurar matplotlib
plt.gray()

# Cargar imagen
image = io.imread('edificio_china.jpg')
M, N = image.shape[:2]

# Calcular DFT-2D
fft = np.fft.fft2(rgb2gray(image))

# Construir matriz de distancias
u = np.arange(M)
v = np.arange(N)
idx = np.where(u > M/2)
u[idx] = u[idx] - M
idx = np.where(v > N/2)
v[idx] = v[idx] - N

V, U = np.meshgrid(v, u)

D = np.sqrt(U**2 + V**2)

# Aplicar filtro
D0 = 20
H = np.double(D > D0)


freq_result = fft * H

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

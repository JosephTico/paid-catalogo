from skimage import io
import matplotlib.pyplot as plt

# Cargar imagen
image = io.imread('peppers.jpg')

# Mostrar imagen
plt.subplot(2, 1, 1)
plt.title('Imagen')
plt.imshow(image, cmap='gray', vmin=0, vmax=255)

# Mostrar histograma
plt.subplot(2, 1, 2)
plt.title('Histograma')
plt.hist(image.ravel(), bins = 256, range=(0, 255))

plt.show()
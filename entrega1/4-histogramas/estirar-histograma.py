from skimage import io
import matplotlib.pyplot as plt

# Cargar imagen
image = io.imread('sydney.jpg', True)
# Estirar imagen
image_stretched = [(255 - 0) / (image.max() - image.min())] * (image - image.min())

# Mostrar imagen original
plt.subplot(2, 2, 1)
plt.title('Imagen original')
plt.imshow(image, cmap='gray', vmin=0, vmax=255)

# Mostrar imagen con histograma estirado
plt.subplot(2, 2, 2)
plt.title('Imagen con histograma estirado')
plt.imshow(image_stretched, cmap='gray', vmin=0, vmax=255)

# Histograma original
plt.subplot(2, 2, 3)
plt.title('Histograma original')
plt.hist(image.ravel(), bins = 256, range=(0, 255))

# Histograma estirado
plt.subplot(2, 2, 4)
plt.title('Histograma estirado')
plt.hist(image_stretched.ravel(), bins = 256, range=(0, 255))

plt.show()
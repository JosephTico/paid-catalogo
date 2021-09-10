from skimage import io

import matplotlib.pyplot as plt

image = io.imread('peppers.jpg')
ax = plt.hist(image.ravel(), bins = 256)
plt.show()
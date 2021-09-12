import cv2
import matplotlib.pyplot as plt
import numpy as np

image0 = cv2.imread("boat.jpg")
plt.subplot(1,2,1)
plt.imshow(image0, cmap='gray')

image0.astype(np.double)
new_image = np.zeros(image0.shape, image0.dtype)
gamma = 1.9
c = 1

for y in range(image0.shape[0]):
  for x in range(image0.shape[1]):
    new_image[y,x] = np.clip(c * (image0[y,x] ** gamma), 0, 255)

new_image.astype(np.uint8)
plt.subplot(1,2,2)
plt.imshow(new_image, cmap='gray')
plt.show()
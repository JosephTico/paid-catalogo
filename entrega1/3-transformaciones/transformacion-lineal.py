import cv2
import matplotlib.pyplot as plt
import numpy as np


image0 = cv2.imread("boat.jpg",0)
#plt.figure()
plt.subplot(1,2,1)
plt.imshow(image0, cmap='gray')
# plt.title('original image')

new_image = np.zeros(image0.shape, image0.dtype)
alpha = 1.8 
beta = 0 

for y in range(image0.shape[0]):
  for x in range(image0.shape[1]):
    new_image[y,x] = np.clip(alpha*image0[y,x] + beta, 0, 255)

plt.subplot(1,2,2)
plt.imshow(new_image, cmap='gray')
# plt.plot(image1)
plt.show()
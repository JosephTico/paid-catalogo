import cv2
import matplotlib.pyplot as plt
import numpy as np


image0 = cv2.imread("child.jpg",0)
#plt.figure()
plt.subplot(2,2,1)
plt.imshow(image0, cmap='gray')
# plt.title('original image')

dest = cv2.Laplacian(image0, cv2.CV_16S, ksize=1)
new_image = cv2.convertScaleAbs(dest)

plt.subplot(2,2,2)
plt.imshow(new_image, cmap='gray')

c = 1
result_image = np.zeros(image0.shape)
for y in range(image0.shape[0]):
  for x in range(image0.shape[1]):
    result_image[y,x] = np.clip((image0[y,x] + c* new_image[y,x]), 0, 255)
plt.subplot(2,2,4)
plt.imshow(result_image, cmap='gray')

plt.show()
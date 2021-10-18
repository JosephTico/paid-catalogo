import cv2
import matplotlib.pyplot as plt
import numpy as np

noise_img1 = cv2.imread("edificio_ruido.jpg",0)
plt.subplot(1,2,1)
plt.imshow(noise_img1, cmap='gray')

noise_img = noise_img1.astype(np.double)

m = np.size(noise_img, 0)
n = np.size(noise_img, 1)

# *** Coeficiente R ***
R = 1
ksize = (3,3)

num = np.power(noise_img, R + 1)
denom = np.power(noise_img, R)
kernel = np.full(ksize, 1.0)
result_image = cv2.filter2D(num, -1, kernel) / cv2.filter2D(denom, -1, kernel)


plt.subplot(1,2,2)
plt.imshow(result_image.astype('uint8'), cmap='gray')

plt.show()
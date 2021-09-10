import cv2
import matplotlib.pyplot as plt
import numpy as np


image0 = cv2.imread("boat.jpg",0)
#plt.figure()
plt.subplot(1,2,1)
plt.imshow(image0, cmap='gray')
# plt.title('original image')

new_image = np.zeros(image0.shape, image0.dtype)
alpha = 1.0 
beta = 100 

#image1= 1*image0+100
new_image = 1*image0 + 50

plt.subplot(1,2,2)
plt.imshow(new_image, cmap='gray')
# plt.plot(image1)
plt.show()
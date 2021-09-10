import cv2
import matplotlib.pyplot as plt
# Count the number of pixels of each gray value


image0 = cv2.imread("boat.jpg",0)
plt.figure()
plt.subplot(1,2,1)

plt.imshow(image0)
plt.title('original image')


image1=image0
plt.subplot(1,2,2)
plt.imshow(image1,vmin=0, vmax=255,cmap = plt.cm.gray)
plt.plot(image1)
plt.show()
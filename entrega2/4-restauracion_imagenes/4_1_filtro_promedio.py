import cv2
import matplotlib.pyplot as plt
import numpy as np

noise_img1 = cv2.imread("edificio_ruido.jpg",0)
plt.subplot(1,2,1)
plt.imshow(noise_img1, cmap='gray')

noise_img = noise_img1.astype(np.double)

m = np.size(noise_img, 0)
n = np.size(noise_img, 1)

result_image = np.zeros(noise_img.shape,noise_img.dtype)

#Filtro Promedio Centro
for x in range(1,m-1):
  for y in range(1,n-1):
    Wf1 = noise_img[x-1,y-1] + noise_img[x-1,y] + noise_img[x-1,y+1]
    Wf2 = noise_img[x,y-1] + noise_img[x,y] + noise_img[x,y+1]
    Wf3 = noise_img[x+1,y-1] + noise_img[x+1,y] + noise_img[x+1,y+1]
    result_image[x,y] = (1/9)*(Wf1+Wf2+Wf3)

#Filtro Promedio Esquinas
result_image[0,0] = (1/4)*(noise_img[0,0] + noise_img[0,1] + noise_img[1,0] + noise_img[1,1])
result_image[m-1,0] = (1/4)*(noise_img[m-1,0] + noise_img[m-1,1] + noise_img[m-2,0] + noise_img[m-2,1])
result_image[0,n-1] = (1/4)*(noise_img[0,n-1] + noise_img[0,n-2] + noise_img[1,n-1] + noise_img[1,n-2])
result_image[m-1,n-1] = (1/4)*(noise_img[m-1,n-1] + noise_img[m-1,n-2] + noise_img[m-2,n-1] + noise_img[m-2,n-2])

# Primera y Ultima Columna
for y in range(1,n-1):
  Uf1 = noise_img[0,y-1] + noise_img[0,y] + noise_img[0,y+1]
  Uf2 = noise_img[1,y-1] + noise_img[1,y] + noise_img[1,y+1]
  result_image[0,y] = (1/6)* (Uf1+Uf2)
  Df1 = noise_img[m-1,y-1] + noise_img[m-1,y] + noise_img[m-1,y+1]
  Df2 = noise_img[m-2,y-1] + noise_img[m-2,y] + noise_img[m-2,y+1]
  result_image[m-1,y] = (1/6)* (Df1+Df2)

# Primera y Ultima Fila
for x in range(1,m-1):
  Lf1 = noise_img[x-1,0] + noise_img[x,0] + noise_img[x+1,0]
  Lf2 = noise_img[x-1,1] + noise_img[x,1] + noise_img[x+1,1]
  result_image[x,0] = (1/6)* (Lf1+Lf2)
  Rf1 = noise_img[x-1,n-1] + noise_img[x,n-1] + noise_img[x+1,n-1]
  Rf2 = noise_img[x-1,n-2] + noise_img[x,n-2] + noise_img[x+1,n-2]
  result_image[x,n-1] = (1/6)* (Rf1+Rf2)

plt.subplot(1,2,2)
plt.imshow(result_image.astype('uint8'), cmap='gray')

plt.show()
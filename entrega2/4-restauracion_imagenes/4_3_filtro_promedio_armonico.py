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
    cont = 0
    if(noise_img[x-1,y-1] != 0): cont+= 1/noise_img[x-1,y-1]
    if(noise_img[x-1,y] != 0): cont+= 1/noise_img[x-1,y]
    if(noise_img[x-1,y+1] != 0): cont+= 1/noise_img[x-1,y+1]
    if(noise_img[x,y-1] != 0): cont+= 1/noise_img[x,y-1] 
    if(noise_img[x,y] != 0): cont+= 1/noise_img[x,y]
    if(noise_img[x,y+1] != 0): cont+= 1/noise_img[x,y+1]
    if(noise_img[x+1,y-1] != 0): cont+= 1/noise_img[x+1,y-1]
    if(noise_img[x+1,y] != 0): cont+= 1/noise_img[x+1,y]
    if(noise_img[x+1,y+1] != 0): cont+= 1/noise_img[x+1,y+1]
    if(cont != 0): result_image[x,y] = 9/cont
#Filtro Promedio Esquinas
cont1=0
if(noise_img[0,0] != 0): cont1+=1/noise_img[0,0]
if(noise_img[0,1] != 0): cont1+=1/noise_img[0,1]
if(noise_img[1,0] != 0): cont1+=1/noise_img[1,0]
if(noise_img[1,1] != 0): cont1+=1/noise_img[1,1]
if(cont1 != 0): result_image[0,0] = 4/cont1
cont2=0
if(noise_img[m-1,0] != 0): cont2+=1/noise_img[m-1,0] 
if(noise_img[m-1,1] != 0): cont2+=1/noise_img[m-1,1]
if(noise_img[m-2,0] != 0): cont2+=1/noise_img[m-2,0]
if(noise_img[m-2,1] != 0): cont2+=1/noise_img[m-2,1]
if(cont2 != 0): result_image[m-1,0] = 4/cont2
cont3=0
if(noise_img[0,n-1] != 0): cont3+=1/noise_img[0,n-1]
if(noise_img[0,n-2] != 0): cont3+=1/noise_img[0,n-2]
if(noise_img[1,n-1] != 0): cont3+=1/noise_img[1,n-1]
if(noise_img[1,n-2] != 0): cont3+=1/noise_img[1,n-2]
if(cont3 != 0): result_image[0,n-1] = 4/cont3
cont4=0
if(noise_img[m-1,n-1] != 0): cont4+=1/noise_img[m-1,n-1]
if(noise_img[m-1,n-2] != 0): cont4+=1/noise_img[m-1,n-2]
if(noise_img[m-2,n-1] != 0): cont4+=1/noise_img[m-2,n-1]
if(noise_img[m-2,n-2] != 0): cont4+=1/noise_img[m-2,n-2]
if(cont4 != 0): result_image[m-1,n-1] = 4/cont4

# Primera y Ultima Columna
for y in range(1,n-1):
  cont1=0
  if(noise_img[0,y-1] != 0): cont1+= 1/noise_img[0,y-1]
  if(noise_img[0,y] != 0): cont1+= 1/noise_img[0,y]
  if(noise_img[0,y+1] != 0): cont1+= 1/noise_img[0,y+1]
  if(noise_img[1,y-1] != 0): cont1+= 1/noise_img[1,y-1]
  if(noise_img[1,y] != 0): cont1+= 1/noise_img[1,y]
  if(noise_img[1,y+1] != 0): cont1+= 1/noise_img[1,y+1]
  if(cont1 != 0): result_image[0,y] = 6/cont1
  cont2=0
  if(noise_img[m-1,y-1] != 0): cont2+= 1/noise_img[m-1,y-1]
  if(noise_img[m-1,y] != 0): cont2+= 1/noise_img[m-1,y]
  if(noise_img[m-1,y+1] != 0): cont2+= 1/noise_img[m-1,y+1]
  if(noise_img[m-2,y-1] != 0): cont2+= 1/noise_img[m-2,y-1]
  if(noise_img[m-2,y] != 0): cont2+= 1/noise_img[m-2,y]
  if(noise_img[m-2,y+1] != 0): cont2+= 1/noise_img[m-2,y+1]
  if(cont2 != 0): result_image[m-1,y] = 6/cont2

# Primera y Ultima Fila
for x in range(1,m-1):
  cont1=0
  if(noise_img[x-1,0] != 0): cont1+= 1/noise_img[x-1,0]
  if(noise_img[x,0] != 0): cont1+= 1/noise_img[x,0]
  if(noise_img[x+1,0] != 0): cont1+= 1/noise_img[x+1,0]
  if(noise_img[x-1,1] != 0): cont1+= 1/noise_img[x-1,1]
  if(noise_img[x,1] != 0): cont1+= 1/noise_img[x,1]
  if(noise_img[x+1,1] != 0): cont1+= 1/noise_img[x+1,1]
  if(cont1 != 0): result_image[x,0] = 6/cont1
  cont2+0
  if(noise_img[x-1,n-1] != 0): cont2+= 1/noise_img[x-1,n-1]
  if(noise_img[x,n-1] != 0): cont2+= 1/noise_img[x,n-1]
  if(noise_img[x+1,n-1] != 0): cont2+= 1/noise_img[x+1,n-1]
  if(noise_img[x-1,n-2] != 0): cont2+= 1/noise_img[x-1,n-2]
  if(noise_img[x,n-2] != 0): cont2+= 1/noise_img[x,n-2]
  if(noise_img[x+1,n-2] != 0): cont2+= 1/noise_img[x+1,n-2]
  if(cont2 != 0): result_image[x,n-1] = 6/cont2

plt.subplot(1,2,2)
plt.imshow(result_image.astype('uint8'), cmap='gray')

plt.show()
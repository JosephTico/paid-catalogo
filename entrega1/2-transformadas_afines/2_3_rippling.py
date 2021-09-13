import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def imageToArray(filename:str, rgb:bool=False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array

def rippling(A:np.array,Ax=15,Ay=15,Lx=75,Ly=75):
    result = np.zeros(A.shape,dtype=np.uint8)
    M, N = A.shape[0],A.shape[1]
    for x in range(M):
        for y in range(N):
            x_new=round(x+Ax*np.sin(2*np.pi*y/Lx))
            y_new=round(y+Ay*np.sin(2*np.pi*x/Ly))
            if (x_new>=0 and  x_new<M and y_new>=0 and  y_new<N ):
                result[x_new][y_new]=A[x][y]
    return result

A = imageToArray("WingedFigure.jpg")
B=rippling(A,Ax=15,Ay=15,Lx=200,Ly=200)


plt.subplot(1, 2, 1)
plt.title('Imagen original')
plt.imshow(A, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.title('Imagen transformada')
plt.imshow(B, cmap='gray', vmin=0, vmax=255)
plt.show()


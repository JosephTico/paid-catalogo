import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def imageToArray(filename:str, rgb:bool=False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array

def traslation(A:np.array, x:int, y:int):
    result = np.zeros(A.shape, dtype=np.uint8)
    M, N = A.shape[0],A.shape[1]
    for i in range(M):
        for j in range(N):
            new_i=i+y
            new_j=j+x
            if (new_i>=0 and  new_i<M and new_j>=0 and  new_j<N ):
                result[new_i][new_j]=A[i][j]
    return result

A = imageToArray("WingedFigure.jpg")
B = traslation(A, 50,200)


plt.subplot(1, 2, 1)
plt.title('Imagen original')
plt.imshow(A, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.title('Imagen trasladada')
plt.imshow(B, cmap='gray', vmin=0, vmax=255)
plt.show()

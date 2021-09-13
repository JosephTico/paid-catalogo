import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def imageToArray(filename:str, rgb:bool=False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array

def bilateral(A, r, p):
    if(type(p)==int and p>=2):
        Y2=np.array(np.random.randint(255, size=A.shape), dtype=float)
        for k in range(1,p+1):
            Y1=np.matmul(A,Y2)
            Y2=np.matmul(A.T,Y1)
        Q, R = np.linalg.qr(Y2)
        Qr=Q[ : , :r]
        B=np.matmul(A,Qr)
        C=Qr.T
        return (B,C)


A = imageToArray("WingedFigure.jpg")
B,C=bilateral(A,30,p=5)
Ar=np.matmul(B,C)

plt.subplot(1, 2, 1)
plt.title('Imagen original')
plt.imshow(A, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.title('Imagen resultante')
plt.imshow(Ar, cmap='gray', vmin=0, vmax=255)
plt.show()
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def imageToArray(filename:str, rgb:bool=False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array

def rotation(A:np.array, angle:int):
    angle = np.radians(angle)
    result = np.zeros(A.shape, dtype=np.uint8)
    M, N = A.shape[0],A.shape[1]
    xc= M//2
    yc= N//2
    a0 = np.cos(angle) 
    a1 = np.sin(angle)
    b0 = -np.sin(angle)
    b1 = np.cos(angle) 
    for i in range(M):
        for j in range(N):
            new_i=round(b0*(j - xc) + b1 * (i - yc) + yc)
            new_j=round(a0*(j - xc) + a1 * (i - yc) + xc)
            if (new_i>=0 and  new_i<M and new_j>=0 and  new_j<N ):
                result[new_i][new_j]=A[i][j]
    return result
def medianFilterBN(A:np.array):
    result = np.zeros(A.shape, dtype=np.uint8)
    M, N = A.shape[0],A.shape[1]
    # esquinas
    result[0][N-1] = np.median([A[0][N-1],
                                A[1][N-1],
                                A[0][N-2]])
    result[M-1][0] = np.median([A[M-2][0],
                                A[M-1][0],
                                A[M-1][1]])
    result[M-1][N-1] = np.median([A[M-1][N-1],
                                  A[M-2][N-1],
                                  A[M-1][N-2]])
    result[0][0] = np.median([A[0][0],
                              A[0][1],
                              A[1][0]])
    for y in range(1,N-1):
        result[0][y] = np.median(A[0:2,y-1:y+1])
        result[M-1][y] = np.median(A[M-2:M,y-1:y+1])
    for x in range(1,M-1):
        result[x][0] = np.median(A[x-1:x+2,:2])
        result[x][N-1] = np.median(A[x-1:x+2,-2:])
        for y in range(1,N-1):
            result[x][y] = np.median(A[x-1:x+2,y-1:y+2])
    return result


A = imageToArray("WingedFigure.jpg")
B = rotation(A, 35)
C = medianFilterBN(B)


plt.subplot(1, 3, 1)
plt.title('Imagen original')
plt.imshow(A, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 3, 2)
plt.title('Imagen rotada')
plt.imshow(B, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 3, 3)
plt.title('Imagen rotada y filtrada')
plt.imshow(C, cmap='gray', vmin=0, vmax=255)
plt.show()
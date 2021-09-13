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

def ripplingAnimation(A, filename="out.gif", minA=0, maxA=50, step=5,Lx=200,Ly=200):
    images=[]
    for a in range(minA, maxA, step):
        images.append(rippling(A,Ax=a,Ay=a,Lx=Lx,Ly=Ly))
    B_img=list(map(Image.fromarray, images))
    B_img[0].save(filename,save_all=True, append_images=B_img[1:], loop=0)   

A_color=imageToArray("WingedFigure.jpg", rgb=True)
ripplingAnimation(A_color, filename="rippling.gif", minA=0, maxA=100, step=5,Lx=200,Ly=200)
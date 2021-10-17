
import cv2
import numpy as np

matrix = [[1,2,3,4,5,6],
          [6,5,4,3,2,1],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [6,5,4,3,2,1],
          [1,2,3,4,5,6]]
kernel = [[1,2,3,4],[1,2,2,1],[1,2,2,1],[4,3,2,1]]

print(matrix)

kl = len(kernel)
ks = (kl-1)/2 ## kernels usually square with odd number of rows/columns
imx = len(matrix)
imy = len(matrix[0])
for i in range(imx):
  for j in range(imy):
    acc = 0
    for ki in range(kl): ##kernel is the matrix to be used
      for kj in range(kl):
        if 0 <= i-ks <= kl: ## make sure you don't get out of bound error
          acc = acc + (matrix[i-ks+ki][j-ks+kj] * kernel[ki][kj]) 
  matrix[i][j] = acc

print("Convolucion:")
print(matrix)

import cv2
import numpy as np

matrix = np.matrix([[1,2,3,4,5,6],
          [6,5,4,3,2,1],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [6,5,4,3,2,1],
          [1,2,3,4,5,6]])
kernel = np.matrix([[1,2,3],[1,2,2],[1,2,2]])



def convolve2D(image, kernel, padding=0, strides=1):
    # Se le da vuelta al Kernel
    kernel = np.flipud(np.fliplr(kernel))
    # Forma del Kernel + Imagen + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]
    # Forma de Salida
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))
    # Aplica Padding Uniforme en todos los lados
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Itera sobre imagen
    for y in range(image.shape[1]):
        # Condicion de salida
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Siguiente fila
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output
print('Matriz:')  
print(matrix)
print('Kernel:')
print(kernel)
print("Convolucion:")
print(convolve2D(matrix,kernel))
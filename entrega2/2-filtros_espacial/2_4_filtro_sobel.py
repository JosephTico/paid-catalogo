import cv2
import matplotlib.pyplot as plt
import numpy as np

def convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output
    
image0 = cv2.imread("baby_yoda.jpg",0)

plt.subplot(1,2,1)
plt.imshow(image0, cmap='gray')

filter_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
filter_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

filtered_image_x = convolve2D(image0, filter_x)
filtered_image_y = convolve2D(image0, filter_y)

result_image = np.zeros(filtered_image_y.shape)
for y in range(filtered_image_y.shape[0]):
  for x in range(filtered_image_y.shape[1]):
    result_image[y,x] = np.clip((np.sqrt((filtered_image_x[y,x]**2)+(filtered_image_y[y,x]**2))), 0, 255)

plt.subplot(1,2,2)
plt.imshow(result_image, cmap='gray')


plt.show()
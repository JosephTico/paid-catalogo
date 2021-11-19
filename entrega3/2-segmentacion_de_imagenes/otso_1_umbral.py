# Implementar dicho métodos para obtener la segmentación de una imagen
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from PIL import Image, ImageOps

def imageToArray(filename: str, rgb: bool = False):
    img = Image.open(filename)
    if not rgb:
        img = ImageOps.grayscale(img)
    img_array = np.array(img)
    return img_array

A = imageToArray("imagen4.jpg")

plt.subplot(2, 4, 1)
plt.title('Imagen Original')
plt.imshow(A, cmap='gray')

m, n = A.shape

# Histograma de la imagen original
plt.subplot(2,2,2);
plt.title('Histograma Original')
plt.hist(A.ravel(), bins = 256, range=(0, 256))

# Umbral basico global
T = 165; iter = 16;
for k in range (1,iter):
  # Mascaras de los bloques
  I1 = (A>T) * 1;
    # Matriz binaria, donde I1(i,j)=1 si A(i,j)>T
  I2 = (A<=T) * 1; 
  # Matriz binaria, donde I1(i,j)=1 si A(i,j)<=T
  B1 = A*I1  # Bloque 1, donde se cumple que B1(i,j)=A(i,j), si A(i,j)>T;
             #                               B1(i,j)=0, si A(i,j)<=T;
  B2 = A*I2;            
  m1 = sum(sum(B1))/sum(sum(I1)); # Promedio de intensidad del Bloque 1   
  m2 = sum(sum(B2))/sum(sum(I2)); # Promedio de intensidad del Bloque 1     
  T = 0.5*(m1+m2);

C = np.zeros((3,5));
C = (A>T) * 1;

plt.subplot(2,2,3);
plt.imshow(C, cmap='gray')
plt.title('Umbral Basico T=' + str(T));

# Umbral metodo de Otsu
# Paso 0: Calcular el histograma de la imagen A
[q,_] = np.histogram(A, bins=256, range=(0, 255))

# Paso 1: Calcular el histograma normalizado
h = (1/(m*n))
h = (h*q)
print(h)

# Paso 2: Calcular vector de suma acumulada
p = np.zeros((256,1))
for k in range (0,256):
  p[k] = np.sum(h[0:k])

# Paso 3: Calcular vector de suma acumulada con peso
mc = np.zeros((256,1))
for k in range(0,256):
  temp = np.arange(start=0, stop=k)
  temp = temp.transpose()
  mc[k] = np.sum(h[0:k]*temp) 

# Paso 4: Calcular el maximo de mc
mg = mc[255];
print("mg:"+str(mg))

# Paso 5: Calcular vector de varianza entre clases
N = mg*p
N = np.subtract(N,mc)
N = np.power(N,2)

D = p*(1-p)

delta2b = np.divide(N,D,out=np.zeros_like(N), where=D!=0)

# Paso 6: Posicion maxima del vector delta2b
T = np.argmax(delta2b)
print("T:"+str(T))

# Mostrar imagen
D = np.zeros((m,n));
D = (A>T) * 1;
plt.subplot(2,2,4);
plt.imshow(D, cmap='gray');
plt.title('Umbral Otsu T=' + str(T));

plt.show()

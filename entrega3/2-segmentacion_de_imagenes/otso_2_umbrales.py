# Implementar dicho métodos para obtener la segmentación de una imagen

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
print("mg"+str(mg))

# Paso 5: Para k1 = 0,1,...,255 y k2 = 0,1,...,255
sigma2b = np.zeros((256,256));
for k1 in range(0,256):
  for k2 in range(0,256):
    if (k1<k2):
      # Paso 6: Calcular P1, P2 y P3
      P1 = np.sum(h[0:k1]);
      
      P2 = np.sum(h[k1:k2]);
      P3 = np.sum(h[k2:256]);
      
      # Paso 7: Calcular m1, m2 y m3
      resultado = 0;
      if (P1!=0):
        temp = np.arange(start=0, stop=k1)
        temp = temp.transpose()
        m1 = (1/P1)*np.sum(temp*h[0:k1])
        resultado += P1 * np.power((m2-mg),2)
      
      if (P2!=0):
        temp = np.arange(start=k1, stop=k2)
        temp = temp.transpose()
        m2 = (1/P2)*np.sum(temp*h[k1:k2])
        resultado += P2 * np.power((m2-mg),2)
      
      if (P3!=0):
        temp = np.arange(start=k2, stop=256)
        temp = temp.transpose()
        m3 = (1/P3)*np.sum(temp*h[k2:256])
        resultado += P3 * np.power((m3-mg),2)

      # Paso 8: Establecer el valor de sigma_b2 para la posicion correspondiente
      sigma2b[k1,k2] = resultado;


# Paso 9: Obtener los umbrales T1, T2

F = sigma2b.max(0)
X = sigma2b.argmax(0)
Z = F.max(0)
T2 = F.argmax(0) 
T1 = X[T2];
T1 = T1-1; 
T2 = T2-1;

# T1 = 166
# T2 = 189

print(str(T1) + ' ' + str(T2))

C = np.zeros((m,n))

for i in range(0,m):
  for j in range(0,n):
    if T1<A[i,j]<T2:
      C[i,j] = 0.5
    elif (A[i,j]<=T1):
      C[i,j] = 0
    else:
      C[i,j] = 1

plt.subplot(2,2,4);
plt.imshow(C, cmap='gray');
plt.title('Umbral Compuesto Otsu: T1=' + str(T1) + ' T2=' + str(T2));

plt.show()

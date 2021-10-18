pkg load image;

% Filtro Ideal (Paso Bajo)
clc; clear; close all;
I = imread('penguin.png');
subplot(2, 2, 1);
imshow(I);
title('Imagen original');
I = im2double(I);
  
% Almacenar tamaño de la imagen
[M, N] = size(I);
  
% Calcular DFT-2D 
F = fft2(I);
subplot(2, 2, 2);
imshow(log(1+abs(F)), []);
title('DFT-2D');

% Frecuencia de corte
D0 = 30; 
  
% Calcular matriz de distancia
u = 0:(M-1);
idx = find(u>M/2);
u(idx) = u(idx)-M;
v = 0:(N-1);
idy = find(v>N/2);
v(idy) = v(idy)-N;
  
[V, U] = meshgrid(v, u);
  
D = sqrt(U.^2+V.^2);
  
% Filtro ideal
H = D <= D0;
  
% Convolución
G = H.*F;

# Graficar DFT-2D filtrado
subplot(2, 2, 3);
imshow(log(1+abs(fftshift(G))), [])
title('DFT-2D con el filtro ideal')
  
% Graficar imagen resultante
output_image = real(ifft2(G));
subplot(2, 2, 4);
imshow(output_image);
title('Imagen con el filtro ideal');
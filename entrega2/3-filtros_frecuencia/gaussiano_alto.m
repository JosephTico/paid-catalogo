pkg load image;

% Filtro Gaussiano (Paso Alto)
clc; clear; close all;
I = imread('edificio_china.jpg');
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



% Calcular matriz de distancia
D = zeros(M, N);
P = floor(M/2); Q = floor(N/2);
for i = 1:M
  for j = 1:N
    D(i, j) = sqrt((i-P)^2 + (j-Q)^2);
  endfor
endfor

% Sigma
S = 10;
  
% Filtro Gaussiano
H = 1-exp(-(D.^2)/(2*S^2)); 
H = fftshift(H);

% Convolución
G = H.*F;

% Graficar DFT-2D filtrado
subplot(2, 2, 3);
imshow(log(1+abs(fftshift(G))), [])
title('DFT-2D con el filtro Gaussiano')
  
% Graficar imagen resultante
output_image = real(ifft2(G));
subplot(2, 2, 4);
imshow(output_image);
title('Imagen con el filtro Gaussiano');
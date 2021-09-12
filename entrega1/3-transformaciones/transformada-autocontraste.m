clc;
clear;
close all;

A = imread('boat_new.jpg');
subplot(1,2,1);
imshow(A)
title('Imagen original');

A = double(A);
[m,n] = size(A);
B = zeros(m,n);

% Valores del nuevo contraste
rmin = min(min(A)); % Extrae valor de las columnas
rmax = max(max(A));

alpha = 255 / (rmax - rmin);
beta = rmin;

B = alpha * (A - beta);


B = uint8(B);
subplot(1,2,2);
imshow(B)
title('Imagen Modificada');
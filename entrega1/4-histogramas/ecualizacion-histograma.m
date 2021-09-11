clc
clear
close all

A = imread('peppers.jpg');
subplot(2,2,1);
imshow(A)
title('Imagen original');


% Calcular el histograma
h2 = zeros(256, 1);
[m, n] = size(A);
for i = 1:255
  h2(i + 1) = sum(sum(A == i));
endfor
subplot(2,2,2);
bar(0:255, h2)
title('Histograma');
xlim([0 255])

% Calcular la distribucion acumulativa
[m, n] = size(A);
v_ac = zeros(256, 1);
for i = 0:255
  v_ac(i + 1) = sum(h2(1:i+1)/(m*n));
endfor
subplot(2,2,3)
bar(0:255, v_ac)
title('Distribucion acumulativa');
xlim([0 255])

% Metodos de ecualizacion
B = zeros(m, n);
A = double(A);
for x = 1:m
  for y = 1:n
    B(x, y) = round(v_ac(A(x, y) + 1) * 255);
  endfor
endfor

B = uint8(B);
subplot(2,2,4);
imshow(B)
title('Imagen ecualizada');
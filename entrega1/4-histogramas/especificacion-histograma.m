clc
clear
close all

A = imread('peppers.jpg');
subplot(4,2,1);
imshow(A)
title('Imagen original');

B = imread('sydney.jpg');
subplot(4,2,2);
imshow(B)
title('Imagen estandar');


% Calcular el histograma original
h1 = zeros(256, 1);
[m, n] = size(A);
for i = 1:255
  h1(i + 1) = sum(sum(A == i));
endfor
subplot(4,2,3);
bar(0:255, h1)
title('Histograma original');
xlim([0 255])

% Calcular el histograma estandar
h2 = zeros(256, 1);
[m, n] = size(B);
for i = 1:255
  h2(i + 1) = sum(sum(B == i));
endfor
subplot(4,2,4);
bar(0:255, h2)
title('Histograma estandar');
xlim([0 255])

% Calcular la distribucion acumulativa
[m, n] = size(A);
v_ac = zeros(256, 1);
for i = 0:255
  v_ac(i + 1) = sum(h1(1:i+1)/(m*n));
endfor
subplot(4,2,5)
bar(0:255, v_ac)
title('Distribucion acumulativa original');
xlim([0 255])

% Calcular la distribucion acumulativa
[m2, n2] = size(B);
v2_ac = zeros(256, 1);
for i = 0:255
  v2_ac(i + 1) = sum(h2(1:i+1)/(m2*n2));
endfor
subplot(4,2,6)
bar(0:255, v2_ac)
title('Distribucion acumulativa estandar');
xlim([0 255])

% Metodos de ecualizacion
C = zeros(m, n);
A = double(A);
for x = 1:m
  for y = 1:n
    C(x, y) = round(v2_ac(A(x, y) + 1) * 255);
  endfor
endfor

C = uint8(C);
subplot(4,1,4);
imshow(C)
title('Imagen original con especificacion de histograma estandar');
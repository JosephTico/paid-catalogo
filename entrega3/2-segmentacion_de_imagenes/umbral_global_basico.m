%Umbral Basico
clc;
clear;
close all;
pkg load image;

A = imread('imagen3.jpg');
subplot(2,2,1);
imshow(A);
title('Imagen Original');

A = im2double(A);
[m,n] = size(A);

T = 0.5;
B = zeros(m,n);
B(A>T) = 1;
B(A<=T) = 0;
subplot(2,2,2);
imshow(B);
title(['Imagen Umbral T=' num2str(T)]);

T = 0.5; iter = 15;
for k = 1:iter

  I1 = (A>T);  
  I2 = (A<=T); 
  B1 = A.*I1;  
  B2 = A.*I2;            
  m1 = sum(sum(B1))/sum(sum(I1)); 
  m2 = sum(sum(B2))/sum(sum(I2)); 
  T = 0.5*(m1+m2);
endfor

C = zeros(m,n);
C(A>T) = 1;
C(A<=T) = 0;
subplot(2,2,3);
imshow(C);
title(['Imagen Umbral T=' num2str(T)]);

subplot(2,2,4);
imhist(A);
title('Histograma imagen original');
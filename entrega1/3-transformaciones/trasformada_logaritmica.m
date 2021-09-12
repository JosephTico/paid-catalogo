clc;
clear;
close all;

A = imread('log.jpg');
subplot(1,2,1);
imshow(A)
title('Imagen original');

A = im2double(A);
[m,n] = size(A);
B = zeros(m,n);

c = 0
for c = 0.1:0.1:5
  B = c.*log(1+A);
  subplot(1,2,2);
  imshow(B);
  title(['Imagen Modificada: c = ' num2str(c)]);
  pause(0.05);
endfor
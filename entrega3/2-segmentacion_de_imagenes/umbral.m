%Umbral Basico
clc;
clear;
close all;
pkg load image;

A = imread('imagen1.jpg');
subplot(1,2,1);
imshow(A);
title('Imagen Original');

A = im2double(A);
[m,n] = size(A);

T = 0.5;
B = zeros(m,n);
B(A>T) = 1;
B(A<=T) = 0;
subplot(1,2,2);
imshow(B);
title('Imagen Umbral Simple');
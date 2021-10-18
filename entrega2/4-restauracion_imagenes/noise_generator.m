clear
clc
close all
pkg load image

A = imread ('edificio_china.jpg');
subplot(1,2,1)
imshow(A)

[m,n] = size(A);
alpha = 0.2;
N = alpha * randn(m,n);

A = im2double(A);
B = A + N;
B = im2uint8(B);

subplot(1,2,2)
imshow(B)

imwrite(B,'edificio_ruido.jpg')

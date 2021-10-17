clear
clc
close all
pkg load image

A = imread ('child.jpg');
subplot(1,2,1)
imshow(A)

# Mascara
B = [1 1 1; 1 -8 1; 1 1 1];
A = im2double(A);
C = conv2(A,B,'same');
C = im2uint8(C);

subplot(1,2,2)
imshow(C)

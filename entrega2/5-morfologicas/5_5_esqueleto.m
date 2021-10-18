% Obtener el esqueleto de una imagen binaria

clc; clear; 
close all;
pkg load image;

A = imread('imagenes/imagen9.jpg');
A = im2double(A);
A_bin = A>0.5;


[m,n] = size(A_bin);
B = ones(8);
Xk = A_bin;

Sk_aux = A_bin&~imopen(A_bin,B);
while 1
  Xk = imerode(Xk,B);
  Yk = imopen(Xk,B);
  Sk = Xk&~Yk;  
  
  if Xk == 0
    break;
  endif  
  
  Sk_aux = Sk_aux|Sk;
endwhile

Y = Sk_aux;


subplot(1,3,1);
imshow(A_bin);
title('Imagen A');


subplot(1,3,2);
imshow(Y);
title('Esqueleto')

subplot(1,3,3);
imshow(or(~A_bin,Y));
title('Sobrepuesto')


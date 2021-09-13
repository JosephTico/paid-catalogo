clear;
clc;
close all;
pkg load image;

I_color = imread("WingedFigure.jpg");
A = I_color(:,:,1);

A =im2double(A);
val_sing=diag(A);
[m,n]=size(A);

[U,S,V] =svd(A);

r=50;
Ur= U(:,1:r);
Vr= V(:,1:r);
Sr= S(1:r,1:r);

B=Ur*Sr;
C= Vr';
Ar=B*C;
Ar = im2uint8(Ar);


subplot(1,2,1);
imshow(A)
title('Imagen original');
subplot(1,2,2);
imshow(Ar)
title('Imagen reducida');

error=norm(A-im2double(Ar),'fro');
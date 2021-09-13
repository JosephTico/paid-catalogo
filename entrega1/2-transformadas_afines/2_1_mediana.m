clc; clear;
pkg load image;

A = imread('WingedFigureNoise.jpg');
A = A(:,:,1);

[m,n] = size(A);
B = zeros(m,n);


B(1, 1) = median(A(1:2, 1:2)(:)); 
B(m, 1) = median(A(m-1:m, 1:2)(:));
B(1, n) = median(A(1:2, n-1:n)(:));
B(m, n) = median(A(m-1:m, n-1:n)(:));

for x = 2:m-1
  B(x, 1) = median(A(x-1:x+1, 1:2)(:));
  B(x, n) = median(A(x-1:x+1, n-1:n)(:));
endfor

for y = 2:n-1
  B(1, y) = median(A(1:2,y-1:y+1)(:));
  B(1, y) = median(A(m-1:m,y-1:y+1)(:));
endfor  

for x = 2:m-1
  for y = 2:n-1
    neighborhood = A(x-1:x+1, y-1:y+1); 
    temp = neighborhood(:);
    B(x, y) = median(temp);
  end
end
B = uint8(B);


subplot(1, 2, 1);
imshow(A);
title('Imagen con ruido');

subplot(1, 2, 2);
imshow(B);
title('Imagen resultante');


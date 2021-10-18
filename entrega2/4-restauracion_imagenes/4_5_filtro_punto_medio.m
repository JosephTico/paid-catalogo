%Filtro Punto Medio
clc; 
clear;
pkg load image;

A_input = imread('edificio_china.jpg');
A_input = A_input(:,:,1);


A = imnoise(A_input, 'salt & pepper', 0.02);
A = double(A);

[m,n] = size(A);
B = zeros(m,n);

function result = medium_point(input_array)
    result= (max(input_array) + min(input_array))/2;
endfunction

B(1, 1) = medium_point(A(1:2, 1:2)(:)); 
B(m, 1) = medium_point(A(m-1:m, 1:2)(:));
B(1, n) = medium_point(A(1:2, n-1:n)(:));
B(m, n) = medium_point(A(m-1:m, n-1:n)(:));

for x = 2:m-1
  B(x, 1) = medium_point(A(x-1:x+1, 1:2)(:));
  B(x, n) = medium_point(A(x-1:x+1, n-1:n)(:));
endfor

for y = 2:n-1
  B(1, y) = medium_point(A(1:2,y-1:y+1)(:));
  B(1, y) = medium_point(A(m-1:m,y-1:y+1)(:));
endfor  

for x = 2:m-1
  for y = 2:n-1
    neighborhood = A(x-1:x+1, y-1:y+1); 
    temp = neighborhood(:);
    B(x, y) = medium_point(temp);
  end
end
A = uint8(A);
B = uint8(B);

subplot(1, 2, 1);
imshow(A);
title('Imagen con ruido');

subplot(1, 2, 2);
imshow(B);
title('Imagen resultante');


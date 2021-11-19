% Ejemplo de Umbral
clc; clear; close all;
pkg load image;
A = imread('imagen4.jpg');
subplot(2,2,1);
imshow(A);
title('Imagen original');

[m,n] = size(A);

% Histograma de la imagen original
subplot(2,2,2);
imhist(A);
title('Histograma imagen original');

% Umbral basico global
T = 165; iter = 15;
for k = 1:iter
  % Mascaras de los bloques
  I1 = (A>T);  % Matriz binaria, donde I1(i,j)=1 si A(i,j)>T
  I2 = (A<=T); % Matriz binaria, donde I1(i,j)=1 si A(i,j)<=T
  B1 = A.*I1;  % Bloque 1, donde se cumple que B1(i,j)=A(i,j), si A(i,j)>T;
               %                               B1(i,j)=0, si A(i,j)<=T;
  B2 = A.*I2;            
  m1 = sum(sum(B1))/sum(sum(I1)); % Promedio de intensidad del Bloque 1   
  m2 = sum(sum(B2))/sum(sum(I2)); % Promedio de intensidad del Bloque 1     
  T = 0.5*(m1+m2);
endfor

C = zeros(m,n);
C(A>T) = 1;
C(A<=T) = 0;
subplot(2,2,3);
imshow(C);
title(['Umbral Basico T=' num2str(T)]);

% Umbral metodo de Otsu
% Paso 0: Calcular el histograma de la imagen A
[q,~] = imhist(A);


% Paso 1: Calcular el histograma normalizado
h = (1/(m*n))*q;

% Paso 2: Calcular vector de suma acumulada
p = zeros(256,1);
for k = 1:256
  p(k) = sum(h(1:k));
endfor


% Paso 3: Calcular vector de suma acumulada con peso
mc = zeros(256,1);
for k = 1:256
  mc(k) = sum((0:k-1)'.*h(1:k));  
endfor

% Paso 4: Calcular el maximo de mc
mg = mc(256);
% Paso 5: Calcular vector de varianza entre clases
N = (mg*p-mc).^2;
D = p.*(1-p);
delta2b = N./D;

% Paso 6: Posicion maxima del vector delta2b
[~,T] = max(delta2b);
T
T = T-1; % Ya que Octave cuenta a partir del 1 y no del 0
% Mostrar imagen
D = zeros(m,n);
D(A>T) = 1;
D(A<=T) = 0;
subplot(2,2,4);
imshow(D);
title(['Umbral Otsu T=' num2str(T)]);
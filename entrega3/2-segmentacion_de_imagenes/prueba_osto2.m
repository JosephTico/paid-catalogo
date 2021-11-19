clc; clear; close all;
pkg load image;

function [T1,T2] = otsu2(A)
  % Funcion que implementa el algoritmo de Otsu para 2 umbrales
  % A: imagen original en formato uint8
  % T1: umbral inferior para la imagen A
  % T2: umbral superior para la imagen A
  [m,n] = size(A);

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
  mg

  % Paso 5: Para k1 = 0,1,...,255 y k2 = 0,1,...,255
  sigma2b = zeros(256,256);
  for k1 = 1:256
    for k2 = 1:256
      if k1<k2
        % Paso 6: Calcular P1, P2 y P3
        P1 = sum(h(1:k1));
        P1
        P2 = sum(h(k1+1:k2));
        P3 = sum(h(k2+1:256));
        
        % Paso 7: Calcular m1, m2 y m3
        resultado = 0;
        if P1
          m1 = (1/P1)*sum((0:k1-1)'.*h(1:k1));
          resultado += P1*(m1-mg)^2;
        endif  
        
        if P2
          m2 = (1/P2)*sum((k1:k2-1)'.*h(k1+1:k2));
          resultado += P2*(m2-mg)^2;
        endif  
        
        if P3  
          m3 = (1/P3)*sum((k2:255)'.*h(k2+1:256)); 
          resultado += P3*(m3-mg)^2;
        endif
        
        % Paso 8: Establecer el valor de sigma_b2 para la posicion correspondiente
        sigma2b(k1,k2) = resultado;
      endif  
    endfor
  endfor

  % Paso 9: Obtener los umbrales T1, T2
  [F,X] = max(sigma2b); 
  [Z,T2] = max(F);
  T1 = X(T2);
  T1 = T1-1; T2 = T2-1;
endfunction

% Carga de la imagen original
A = imread('imagen4.jpg');
subplot(1,3,1);
imshow(A);
title('Imagen original')
[m,n] = size(A);


% Umbrales con el metodo de otsu para 2 umbrales
[T1,T2] = otsu2(A);
C = im2double(zeros(m,n));
C(T1<A<T2) = 0.5;
C(A<=T1) = 0;
C(T2<=A) = 1;
subplot(1,3,3);
imshow(C);
title(['Umbral Compuesto Otsu: T1=' num2str(T1) ' T2=' num2str(T2)]);
clc; 
clear; 
close all
pkg load image 

A=imread('edificio_china.jpg'); 

B=imnoise(A,'gaussian');

subplot(1,2,1) 
imshow(B)

A_t=filt_prom_arm(B);

subplot(1,2,2)
imshow(A_t)

function A_t=filt_prom_arm(B)
  
  B=double(B); 
  [m,n]=size(B); 
  A_t=zeros(m,n); 

  %Inversa de la matriz
  Binv=B.^-1;
  mask=isinf(Binv); 
  Binv(mask)=0.0; 

  %Esquinas
  W=Binv(1,1)+Binv(1,2)+Binv(2,1)+Binv(2,2);
  A_t(1,1)=4/W;
  W=Binv(1,n)+Binv(1,n-1)+Binv(2,n)+Binv(2,n-1);
  A_t(1,n)=4/W;
  W=Binv(m,1)+Binv(m,2)+Binv(m-1,1)+Binv(m-1,2);
  A_t(m,1)=4/W;
  W=Binv(m,n)+Binv(m,n-1)+Binv(m-1,n)+Binv(m-1,n-1);
  A_t(m,n)=4/W;


  %Filtrado en bordes horizontales
  for y=2:n-1
    Wnf1=Binv(1,y-1)+Binv(1,y)+Binv(1,y+1); %Fila 1
    Wnf2=Binv(2,y-1)+Binv(2,y)+Binv(2,y+1); %Fila 2
    A_t(1,y)=6/(Wnf1+Wnf2);

    Wnf1=Binv(m-1,y-1)+Binv(m-1,y)+Binv(m-1,y+1); %Fila 1
    Wnf2=Binv(m,y-1)+Binv(m,y)+Binv(m,y+1); %Fila 2
    A_t(m,y)=6/(Wnf1+Wnf2);
  endfor

  %Filtrado en bordes laterales
  for x=2:m-1
    Wnc1=Binv(x-1,n-1)+Binv(x,n-1)+Binv(x+1,n-1); %Col 1
    Wnc2=Binv(x-1,n)+Binv(x,n)+Binv(x+1,n); %Col 2
    A_t(x,n)=6/(Wnc1+Wnc2);

    Wnc1=Binv(x-1,1)+Binv(x,1)+Binv(x+1,1); %Col 1
    Wnc2=Binv(x-1,2)+Binv(x,2)+Binv(x+1,2); %Col 2
    A_t(x,1)=6/(Wnc1+Wnc2);
  endfor

  %Filtrado general
  for x=2:m-1
    for y=2:n-1
      Wf1=Binv(x-1,y-1)+Binv(x-1,y)+Binv(x-1,y+1); %Fila 1
      Wf2=Binv(x,y-1)+Binv(x,y)+Binv(x,y+1); %Fila 2
      Wf3=Binv(x+1,y-1)+Binv(x+1,y)+Binv(x+1,y+1); %Fila 3
      A_t(x,y)=9/(Wf1+Wf2+Wf3);
    endfor
  endfor

  A_t=uint8(A_t);
endfunction
% jpeg compresion matlab 
clear;
clc;
close all;
pkg load image;
pkg load signal;

I_color = imread("WingedFigure.jpg");
A = I_color(:,:,1);


function Q = quantizacion(n)
    Q50=[16 11 10 16 24 40 51 61;
       12 12 14 19 26 58 60 55;
       14 13 16 24 40 57 59 56;
       14 17 22 29 51 87 80 62;
       18 22 37 56 68 109 103 77;
       24 35 55 64 81 104 113 92;
       49 64 78 87 103 121 120 101;
       72 92 95 98 112 100 103 99];
    if n==50
        Q=Q50;
    elseif n==0
        Q=ones(8);
    elseif and(n>50,n<100)
        Q=round(((100-n)/50)*Q50);
    elseif and(n>0, n<50)
        Q=round((50/n)*Q50);
    else
        Q=NaN;
        display("Error");
    endif
endfunction

function Vect=mat2vect_diag(M)
    Vect= ZigZagscan(M);
    #reverse the vector
    while and(Vect(end)==0 , length(Vect)>1)
        Vect=Vect(1:end-1);
    endwhile
endfunction

function Mat=vect2mat_diag(V, n=8)
    size_V=size(V,2);
    V = [V zeros(1,(n*n) - size_V)];
    Mat=izigsc(V,n);
endfunction



%% ordered list
%X = [ 1 2 3;
%      4 5 6;
%      7 8 9];
%ZigZagscan(X)
%
%
%X = [ 1 2 3;
%      4 5 0;
%      0 0 0];
%ZigZagscan(X)
%matzz=mat2vect_diag(X)
%
%vect2mat_diag(matzz)
%
B=[154 123 123 123 123 123 123 136;
192 180 136 154 154 154 136 110;
254 198 154 154 180 154 123 123;
239 180 136 180 180 166 123 123;
180 154 136 167 166 149 136 136;
128 136 123 136 154 180 198 154;
123 105 110 149 136 136 180 166;
110 136 123 123 123 136 154 136];


function [compressed_blocks, rows, cols ]=jpeg_compress(input_img, Q_per=50)
    [M N] = size(input_img);
    rows = floor(M / 8);
    cols = floor(N / 8);
    compressed_blocks={};
    for x = 1:rows
        for y = 1:cols
            n_block=input_img(1 + (8 * (x - 1)):(8 * (x)), 1 + (8 * (y - 1)):(8 * (y)));
            n_block=double(n_block);
            M_block=n_block-128;
            D_block=dct2(M_block);
            Q_block=quantizacion(Q_per);
            C_block=round(D_block./Q_block);
            %C_block
            x_block=mat2vect_diag(C_block);
            compressed_blocks= [compressed_blocks ; {x_block}];
        endfor
    endfor
endfunction


A=A(101:500,101:500);
input_img=A;
n=1;
%[compressed_blocks, rows, cols ]=jpeg_compress(input_img, n);

%save matrix to file
%save("compressed_blocks.mat","compressed_blocks" ,"rows", "cols" , "-mat");

% load("compressed_blocks.mat");

function decompressed_img=jpeg_decompress(compressed_blocks, rows, cols, Q_per=50)
    M = size(compressed_blocks,1);
    decompressed_img=zeros(rows*8, cols*8);
    x_block_index=1;
    for x = 1:rows
        for y = 1:cols
            x_block=compressed_blocks{x_block_index};
            x_block_index++;
            C_block=vect2mat_diag(x_block,8);
            Q_block=quantizacion(Q_per);
            D_block=C_block.*Q_block;
            M_block=idct2(D_block);
            n_block=M_block+128;
            decompressed_img(1 + (8 * (x - 1)):(8 * (x)), 1 + (8 * (y - 1)):(8 * (y)))=n_block;
        endfor
    endfor
    decompressed_img=uint8(decompressed_img);
endfunction



%decompressed_img=jpeg_decompress(compressed_blocks, rows, cols,n);


%subplot(1,2,1);
%imshow(A)
%title('Imagen original');
%subplot(1,2,2);
%imshow(decompressed_img)
%title('Imagen comprimida');
%
%imwrite(decompressed_img, "decompressed_img.jpg");


%for iterate list
subplot(2,4,1);
imshow(A)
title('Imagen original');
plot_n=2
for i= [1 10 25 50 75 85 95]
    n=i
    [compressed_blocks, rows, cols ]=jpeg_compress(input_img, n);
    decompressed_img=jpeg_decompress(compressed_blocks, rows, cols,n);
    subplot(2,4,plot_n);
    plot_n++;
    imshow(decompressed_img)
    title(i);
endfor
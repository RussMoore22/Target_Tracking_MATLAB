clc
clear all
close all

tic

imageNumber = 13;   % Number of images that will be used. does not include Canvas image
imageCategory = 'rocket';   % change to the prefix of each image in imageset

% Everything below does not need to change to accomodate different data

canvas = imread(strcat(imageCategory, 'Canvas.jpg'));


im3DArray = imread(strcat(imageCategory, int2str(1), '.jpg'));

for i = 2:imageNumber
    imStr = strcat(imageCategory, int2str(i), '.jpg');
    im3DArray = stackArrays(im3DArray,imread(imStr), i);
end



im3DArrayDiff = imresize(imfuse(canvas, im3DArray(:,:,1), "diff"), [100,100]);
for i = 2:imageNumber
    im3DArrayDiff = stackArrays(im3DArrayDiff, imresize(imfuse(canvas, im3DArray(:,:,i), "diff"), [100,100]), i);
end



im3DArrayBin = getBinImage(im3DArrayDiff(:,:,1));

for i = 2:imageNumber
    im3DArrayBin = stackArrays(im3DArrayBin, getBinImage(im3DArrayDiff(:,:,i)), i);
end

x = [];
y = [];

[boxArrayi, out1, out2] = getBoundBoxShell(im3DArrayBin);

for i = 2:imageNumber
   [box, x(i), y(i)] = getBoundBoxShell(im3DArrayBin(:,:,i));
   boxArrayi = stackArrays(boxArrayi, box, i);
end


boxArray = imfuse(boxArrayi(:,:,1), im3DArrayDiff(:,:,1));
for i = 2:imageNumber
    boxArray = stackArrays(boxArray, imfuse(boxArrayi(:,:,i), im3DArrayDiff(:,:,i), 'blend'), i);
end
toc



for i = 1:imageNumber
    imshow(im3DArray(:,:,i));
pause(.1);

end

for i = 1:imageNumber
    imshow(imresize(im3DArrayDiff(:,:,i), [1000, 1000]));
pause(.1);

end



for i = [6,10]
    imshow(imresize(boxArray(:,:,i), [1000,1000]));
    pause(10);
end



plot(x,y,'o')
grid
axis([0,100,0,100])
xlabel("X")
ylabel("Y")
title("Estimated 2D Position of Object Center")

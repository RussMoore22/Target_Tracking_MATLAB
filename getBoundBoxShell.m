function [box, x, y] = getBoundBoxShell(inArray)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

lx = uint16(mean(getPoints(inArray, 'l')));
rx = uint16(mean(getPoints(inArray, 'r')));
tx = uint16(mean(getPoints(inArray, 't')));
bx = uint16(mean(getPoints(inArray, 'b')));


C = zeros(size(inArray));

if lx > rx
    temp = lx;
    lx = rx;
    rx = temp;
end


    for j = lx:rx
        try
        C(bx,j) = 255;
        C(tx,j) = 255;
        end 
    end
        for i = tx:bx
        try
        C(i, lx) = 255;
        C(i,rx) = 255;
        end 
    end
x = abs((rx+lx)/2);
y = abs(100-(bx+tx)/2);
box = C;
end








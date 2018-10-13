function [outArray] = stackArrays(A,B,z)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

x = size(B,1);
y = size(B,2);



for i = 1:x
    for j = 1:y
        A(i,j,z) = B(i,j);
    end
end

outArray = A;

end


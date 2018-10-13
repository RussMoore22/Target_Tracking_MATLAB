function [outArray] = getBinImage(inArray)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

%outArray = zeros(size(inArray,1),size(inArray,2));

for i = 1:size(inArray,1)
    for j = 1:size(inArray,2)
        if inArray(i,j) > 150
            outArray(i,j) = 50;
    end
    end
end

end


function [points] = getPoints(inArray,Str)
%UNTITLED8 Summary of this function goes here
%   Detailed explanation goes here


count = 0;
if Str == 'l'
    points = [];
    for i = 1:size(inArray,1)
    for j = 1:size(inArray,2)
        
        if inArray(i,j) ~= 0
            count = count + 1;
            points(count) = j;
            break
        end
    end
    end
end

    
if Str == 'r'
    points = [];
    for i = 1:size(inArray,1)
    for j = size(inArray,2):-1:1
        
        if inArray(i,j) ~= 0
            count = count + 1;
            points(count) = j;
            break
        end
    end
    end
end
    
    
    
    if Str == 't'
        points = [];
    for j = 1:size(inArray,2)
        for i = 1:size(inArray,1)
    
        
        if inArray(i,j) ~= 0
            count = count + 1;
            points(count) = i;
            break
        end
    end
    end
    end
    
    if Str == 'b'
        points = [];
    for j = 1:size(inArray,2)
        for i = size(inArray,1):-1:1
    
        
        if inArray(i,j) ~= 0
            count = count + 1;
            points(count) = i;
            break
        end
    end
    end
    end
    
end


function realClassesDetection = getRealClass(directory)
    [Data, HDR] = getRawData(directory);
    realClassesDetection = HDR.Classlabel;
%    display(realClassesDetection)
    
end
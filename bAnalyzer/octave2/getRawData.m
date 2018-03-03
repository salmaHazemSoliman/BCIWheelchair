
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%6functions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%Return data and hdr to KNNgeneric

function [Data, HDR] = getRawData(filename)


%    disp(filename)
    [DataHeader, RawData]  = getData(filename);
    %%dataheader di 

    [Triggers, ClassesTypes, ClassesNames] = getTriggers(filename);
    
    Data        = RawData(:,2:15);
    HDR.Label   = DataHeader;

    HDR.SampleRate= 128;
    HDR.TRIG        = Triggers;
    HDR.Classlabel  = ClassesTypes;
    HDR.Classnames  = ClassesNames;  

end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%get raw data and headers and properties for train case

function [DataHeader, RawData] = getData(filename)
  
    HeaderLineNumber  = getLineNumber(filename, 'Count');
    
    DataHeader  = getDataHeader(filename, HeaderLineNumber);
    RawData     = csvread(filename, HeaderLineNumber, 0);
    
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%by2rahom mn file ka strings and then y7awelhom matrix by delimiter ','
function [Triggers, ClassesTypes, ClassesNames] = getTriggers(filename)
    Triggers_string      = getAttribute(filename, 'Triggers');
    ClassesTypes_string  = getAttribute(filename, 'ClassesTypes');
    ClassesNames_string  = getAttribute(filename, 'ClassesNames');
    
    
    Triggers_cell       = textscan(Triggers_string, '%d', 'delimiter', ',');
    ClassesTypes_cell   = textscan(ClassesTypes_string, '%d', 'delimiter', ',');
    ClassesNames_cell   = textscan(ClassesNames_string, '%s', 'delimiter', ',');
    
    Triggers     = cell2mat(Triggers_cell);
    ClassesTypes = cell2mat(ClassesTypes_cell);
    ClassesNames = cell2mat(ClassesNames_cell);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%Names of channels
function DataHeader = getDataHeader(filename, HeaderLineNumber)
    fid = fopen(filename);
    
    for k=1:HeaderLineNumber
        DataHeader_string = fgetl(fid);
    end
    
    DataHeader_cell = textscan(DataHeader_string, '%s', 'delimiter', ',');
    DataHeader      = cell2mat(DataHeader_cell);

    fclose(fid);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%get attribute sting ex: class names, classtypes,

function Attribute = getAttribute(filename, text)
    LineNumber = getLineNumber(filename, text);

    fid = fopen(filename);

    AttributeLine = textscan(fid, '%s %s', 1, 'headerlines', LineNumber-1, 'delimiter', ':');
    Attribute = cell2mat(AttributeLine(2){1});    
    
    fclose(fid);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%search for attribute , return lineNumber as index in file to read from thsi line

function LineNumber = getLineNumber(filename, text)
    fid = fopen(filename);
    LineNumber = 1;
    
    while 1
        tline = fgetl(fid);
        if ischar(tline)
            U = strfind(tline, text);
            if isfinite(U) == 1;
                break
            end
        end
        LineNumber = LineNumber + 1;
    end
    
    fclose(fid);
end

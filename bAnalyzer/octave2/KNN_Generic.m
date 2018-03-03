function TrainOut = KNN_Generic(directory, noiseFlag, idealFlag, butterFlag,NoneFilterFlag, f1FLag,f2FLag,f3FLag,f4FLag,f5FLag,f6FLag,LDAFLag,PCAFlag,CSP_LDAFlag,NoneFlag,startD,endD)
%{

example call
use remove noise .. getMuBeta .. PCA .. start at 0 .. end at 4
TrainOut = KNN_Generic("../Osama Mohamed.csv",1,1,0,0,0,0,0,0,1,0,0,0,4 ); 

directory = data file path

f1FLag = getMuBeta
f2Flag = GetMuBeta_more_feature 
f3Flag = GetMuBeta_more_feature2 -> get min Mu, max Beta
f4Flag = GetMuBeta_more_feature3 -> get min Mu, max Beta, mean Mu, mean Beta 
f5Flag = GetMuBeta_more_feature4 -> get min Mu, max Mu, min Beta, max Beta
f6Flag = GetMuBeta_more_feature5 -> get min Mu, max Mu, min Beta, max Beta, mean Mu, mean Beta

LDAFLag = use LDA
PCAFlag = use PCA
CSP_LDAFlag = use CSP then LDA
NoneFlag = use CSP 


signal starts at 3 and ends at 7 (4 seconds)
startD = start time for the trial enter number between 3 to 7 
endD = end of trial signal
%}
pkg load geometry


        startD = int32(startD);
        endD = int32(endD);

	% Get Raw Data from the file 
	[data, HDR] = getRawData(directory);
  
        HDR.TRIG = HDR.TRIG +1;
        % Intial values
        Classes = HDR.Classnames;
        nClass = length(Classes);
        classes_no =[];
        for g = 1:nClass
            classes_no = [ classes_no , getClassNumber(HDR,Classes(g)) ];
        end
	% Intial values
        
	% do pre-processing here please 
	if(noiseFlag == 1)
		noise = mean(data')';
		data =  data -noise;	
	endif
        %%calculate the centered Data
	% Get features (mu & beta) according to the selected method
	if(NoneFilterFlag == 1)
            if(f1FLag == 1)
                [Mu,Beta] = NoFilter_Train(data, HDR,startD, endD);
            elseif(f3FLag == 1)
                [Mu,temp] = NoFilter_Train(data, HDR,startD, endD, @min);
                [temp,Beta] = NoFilter_Train(data, HDR,startD, endD, @max);
            %TODO: support F3 to F6 flags
            endif
endif


if(idealFlag == 1)
                             
            if(f1FLag == 1)
                [Mu,Beta] = idealFilter_Train(data, HDR,startD, endD);
            elseif(f3FLag == 1)

                [Mu,temp] = idealFilter_Train(data, HDR,startD, endD, @min);
                [temp,Beta] = idealFilter_Train(data, HDR,startD, endD, @max);
            %TODO: support F3 to F6 flags
            endif
endif
        
if(butterFlag == 1)
    if(f1FLag == 1)
            x = "before filter";
            [Mu,Beta] =  GetMuBeta(startD, endD, data, HDR);
              
    elseif (f2FLag == 1)
            [Mu,Beta] =  GetMuBeta_more_feature(startD, endD, data, HDR);
    elseif (f3FLag == 1)
            [Mu,Beta] =  GetMuBeta_more_feature2(startD, endD, data, HDR);
    elseif (f4FLag == 1)
            [Mu,Beta] =  GetMuBeta_more_feature3(startD, endD, data, HDR);
    elseif (f5FLag == 1)
            [Mu,Beta] =  GetMuBeta_more_feature4(startD, endD, data, HDR);
    elseif (f6FLag == 1)
            [Mu,Beta] =  GetMuBeta_more_feature5(startD, endD, data, HDR);
    endif
endif
        
	% apply LDA or PCA or CSP

  kPCA = [];
  kLDA = [];
  kNone = [];
  
  X=[];
  t=[];
	ZLDA = [];
	ZPCA = [];
	VPCA = [];
        VNone = [];
	VLDA = [];
	PC_NumLDA = 0;
	PC_NumPCA = 0;
        PC_NumNone = 0;
        datalength = 0;
	
	if(LDAFLag == 1)
		%LDA
		X = [Mu Beta];
		[ZLDA, VLDA]  = LDA_fn(HDR.Classlabel, X, classes_no);
		PC_NumLDA = [];
    kLDA = [];
            % Get the classifier parameters here
    ClassesData = zeros(size(X)(1)/nClass,PC_NumLDA,nClass);
    for g = 1:nClass
        C1  = ZLDA(HDR.Classlabel == classes_no(g),:);
        C2  = ZLDA(HDR.Classlabel ~= classes_no(g),:);
        Z = [C1; C2];
        t = [ones(size(C1)(1),1) ; -1*ones(size(C2)(1),1)]';
        [accuracy k_total] = knnResults(Z, t);
        [AccSelected, AccIndex] = max(accuracy);
        PC_NumLDA =[PC_NumLDA; min(AccIndex)];
        kLDA =[kLDA; k_total(PC_NumLDA)];
    end
    datalength = size(ZLDA)(1);
	elseif(PCAFlag == 1)
		%PCA
		pureData = [Mu, Beta];
		[VPCA, ZPCA]= pcaProject(pureData);
                % make zpca consistent with zlda!
                ZPCA = ZPCA';
                PC_NumPCA = [];
                kPCA = [];
            % Get the classifier parameters here
                ClassesData = zeros(size(X)(1)/nClass,PC_NumPCA,nClass);
                for g = 1:nClass
                    C1  = ZPCA(HDR.Classlabel == classes_no(g),:);
                    C2  = ZPCA(HDR.Classlabel ~= classes_no(g),:);
                    Z = [C1; C2];
                    t = [ones(size(C1)(1),1) ; -1*ones(size(C2)(1),1)]';
                    [accuracy k_total] = knnResults(Z, t);
                    [AccSelected, AccIndex] = max(accuracy);
                    PC_NumPCA =[PC_NumPCA; min(AccIndex)];
                    kPCA =[kPCA; k_total(PC_NumPCA)];
                end
                
        	datalength = size(ZPCA)(1);		
	
  elseif(CSP_LDAFlag == 1)
		%NOT working to be reviewed with Raghda or Hemaly !
		%CSP then LDA
		
      
	elseif(NoneFlag == 1)
                
		X = [Mu Beta];
                PC_NumNone = [];
                kNone = [];
            % Get the classifier parameters here
                ClassesData = zeros(size(X)(1)/nClass,PC_NumNone,nClass);
                for g = 1:nClass
                    C1  = X(HDR.Classlabel == classes_no(g),:);
                    C2  = X(HDR.Classlabel ~= classes_no(g),:);
                    Z = [C1; C2];
                    t = [ones(size(C1)(1),1) ; -1*ones(size(C2)(1),1)]';
                    [accuracy k_total] = knnResults(Z, t);
                    [AccSelected, AccIndex] = max(accuracy);
                    PC_NumNone =[PC_NumNone; min(AccIndex)];
                    kNone =[kNone; k_total(PC_NumNone)];
                end
                
        	datalength = size(X)(1);
                
	endif
        
	% Returing output structure
        
        %%% adding a new variable to the struct is as easy as the following line
        %TrainOut.lol = "haha";
        %%% if we ever wanted to comment multi-lines, use % instead of %{ and %}
        %--------
        TrainOut.VLDA = VLDA;
        TrainOut.ZtrainLDA = ZLDA;
        TrainOut.PC_NumLDA = PC_NumLDA;
        TrainOut.kLDA = kLDA;
        TrainOut.LDAData = ZLDA;
        %--------
        TrainOut.VPCA = VPCA;
        TrainOut.ZtrainPCA = ZPCA;
        TrainOut.PC_NumPCA = PC_NumPCA;
        TrainOut.kPCA = kPCA;
        TrainOut.PCAData = ZPCA;
        %--------
        TrainOut.VNone = 1;
        TrainOut.ZtrainNone = X;
        TrainOut.PC_NumNone = PC_NumNone;
        TrainOut.kNone = kNone;
        TrainOut.NoneData = Z;
        %--------
	      TrainOut.Classlabel = HDR.Classlabel;
        TrainOut.Classnames = HDR.Classnames;
        TrainOut.nClass = nClass;
        TrainOut.classes_no =  classes_no;
	      %--------
        TrainOut.datalength = datalength;
        TrainOut.ClassesTypes = HDR.Classlabel;
        TrainOut.ClassesTypesSameFile = HDR.Classlabel;

end


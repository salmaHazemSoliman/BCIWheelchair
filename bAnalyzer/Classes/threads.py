import os
import sys
import numpy as np
import oct2py 
import thread
from PyQt4 import QtCore, QtGui
import gspread
import GooglespreadSheetConfig as GSC

from AccuracyStats import AccuracyUtilities as AU

#check http://stackoverflow.com/questions/2827623/python-create-object-and-add-attributes-to-it
class Object(object):
    pass


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class readDataThread(QtCore.QThread):
    def __init__(self,  dataFile,detectFile, removeNoiseFlag,SignalStart, SignalEnd, \
		 selectedFeatureExtractionMethod,selectedPreprocessingMethod,FeatureEnhancementSelectedMethod, classifierSelected, \
		 trainTestFlag = True, selectedData=None, sameFile = True, verbose = False):
        QtCore.QThread.__init__(self)
        self.path = dataFile
	self.sameFile = sameFile
        #write any initialization here
        self.dataFile = str(dataFile)
	self.detectFile = str(detectFile)
	self.accTestResult = 010101

	if (self.detectFile == None):
	    if (self.sameFile):
		self.detectFile = self.path
	    else:
		#detectFile is None while samefile is False !
		print "detectFile is set to None while we're detecting from another file!"

        self.removeNoiseFlag = removeNoiseFlag
        self.SignalStart = int(SignalStart)
        self.SignalEnd = int(SignalEnd)
        self.selectedFeatureExtractionMethod = selectedFeatureExtractionMethod
	self.selectedPreprocessingMethod = selectedPreprocessingMethod
	self.FeatureEnhancementSelectedMethod = FeatureEnhancementSelectedMethod
        self.classifierFile = classifierSelected
	self.selectedData = selectedData
	self.trainTestFlag = trainTestFlag
	self.dataLength = 0
	self.LDAData = []
	self.PCAData = []
        self.octave = oct2py.Oct2Py()
        self.octave.addpath('octave2')
	self.verbose = verbose
	self.TP=0
	self.TN=0
	self.FP=0
	self.FN=0

	

    def run(self):
	#"../Osama Mohamed.csv",1,1,0,0,0,0,0,0,1,0,0,0,4
	
	#TrainOut = KNN_Generic(directory, noiseFlag, f1FLag,f2FLag,f3FLag,f4FLag,f5FLag,f6FLag,LDAFLag,PCAFlag,CSP_LDAFlag,NoneFlag,startD,endD)

	#TODO: change f*FLag to f*Flag!
	#settig the feature selection method flags
	if(self.selectedFeatureExtractionMethod =="mean"):
	    self.f1FLag = 1
	else:
	    self.f1FLag = 0
	if(self.selectedFeatureExtractionMethod =="Min MU and Max Beta"):
	    self.f3FLag = 1
	else:
	    self.f3FLag = 0
	if(self.selectedFeatureExtractionMethod =="Min Mu, Max Beta, Mean Mu, Mean Beta"):
	    self.f4FLag = 1
	else:
	    self.f4FLag = 0
	if(self.selectedFeatureExtractionMethod =="Min Mu Max Mu Min Beta Max Beta"):
	    self.f5FLag = 1
	else:
	    self.f5FLag = 0
	if(self.selectedFeatureExtractionMethod =="Min Mu, max Mu, Min Beta, Max Beta, Mean Mu, Mean Beta"):
	    self.f6FLag = 1
	else:
	    self.f6FLag = 0
	
	#preprocessing is not done yet    
	self.idealFlag = 0
	self.butterFlag = 0
	self.NoneFilterFlag = 0
	if(self.selectedPreprocessingMethod == "ideal"):
	    self.idealFlag = 1
            print("Ideal")
	elif(self.selectedPreprocessingMethod == "butter"):
	    self.butterFlag = 1
	    print("BUTTER")
	elif(self.selectedPreprocessingMethod == "None"):
	    self.NoneFilterFlag = 1
	    print("None")
	else:
	    print "undetermined pre-processing type"

	#setting the feature enhancement flags 
	if(self.FeatureEnhancementSelectedMethod == "PCA"):
	    self.PCAFlag = 1
	else:
	    self.PCAFlag = 0
	if(self.FeatureEnhancementSelectedMethod == "LDA"):
	    self.LDAFlag = 1
	else:
	    self.LDAFlag = 0
	if(self.FeatureEnhancementSelectedMethod == "None"):
	    self.NoneFlag = 1
	else:
	    self.NoneFlag = 0
	    
	#unused flags for now
	self.CSP_LDAFlag =0
	self.f2FLag =0
	
	#define the output structures
	self.knnTrainOut = oct2py.Struct()
	self.fisherTrainOut = oct2py.Struct()
	self.leastSquaresTrainOut = oct2py.Struct()
	self.likelihoodTrainOut = oct2py.Struct()
	self.likelihoodClass  = oct2py.Struct()
	
	
	self.knnResult = oct2py.Struct()
	self.knnResultInput = oct2py.Struct()
	
	self.fisherResult = oct2py.Struct()
	self.fisherResultInput = oct2py.Struct()

	self.likelihoodResult = oct2py.Struct()
	self.likelihoodResultInput = oct2py.Struct()

	self.leastSquaresResult = oct2py.Struct()
	self.leastSquaresResultInput = oct2py.Struct()

	#calling the classifer selected according
	#if (self.trainTestFlag == True):

	if(self.classifierFile == "KNN"):
	    self.knnTrainOut = self.octave.feval('KNN_Generic.m', self.dataFile, self.removeNoiseFlag, self.idealFlag, self.butterFlag,self.NoneFilterFlag, self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag,self.SignalStart,self.SignalEnd)
	    self.LDAData = self.knnTrainOut.LDAData
	    self.PCAData = self.knnTrainOut.PCAData
	    self.NoneData = self.knnTrainOut.NoneData
	    self.dataLength = self.knnTrainOut.datalength
	    print("KNN training done!")
	    
	    ###>--- using either of them is ok for debugging ---<###
	    #print(self.knnTrainOut.KPCA)
	    #print(self.knnTrainOut['KPCA'])

	elif (self.classifierFile == "Fisher"):
            print(self.idealFlag)
            print(self.butterFlag)
	    self.fisherTrainOut = self.octave.feval('Fisher_Generic.m', self.dataFile, self.removeNoiseFlag,self.idealFlag, self.butterFlag,self.NoneFilterFlag, self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag,self.SignalStart,self.SignalEnd)
	    self.LDAData = self.fisherTrainOut.LDAData
	    self.PCAData = self.fisherTrainOut.PCAData
	    self.NoneData = self.fisherTrainOut.NoneData
	    self.dataLength = self.fisherTrainOut.datalength
	    print("Fisher training done!")
    
	elif(self.classifierFile == "Likelihood"):
	    self.likelihoodTrainOut = self.octave.feval('Likelihood_Generic.m', self.dataFile, self.removeNoiseFlag,self.idealFlag, self.butterFlag,self.NoneFilterFlag, self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag,self.SignalStart,self.SignalEnd)
	    self.LDAData = self.likelihoodTrainOut.LDAData
	    self.PCAData = self.likelihoodTrainOut.PCAData
	    self.NoneData = self.likelihoodTrainOut.NoneData
	    self.dataLength = self.likelihoodTrainOut.datalength
	    
	    print("Likelihood training done!")
    
	elif(self.classifierFile == "Least Squares"):
	    self.leastSquaresTrainOut = self.octave.feval('Leastsquares_Generic.m', self.dataFile, self.removeNoiseFlag,self.idealFlag, self.butterFlag,self.NoneFilterFlag, self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag,self.SignalStart,self.SignalEnd)
	    self.LDAData = self.leastSquaresTrainOut.LDAData
	    self.PCAData = self.leastSquaresTrainOut.PCAData
	    self.NoneData = self.leastSquaresTrainOut.NoneData
	    self.dataLength = self.leastSquaresTrainOut.datalength
	    print("Least Square training done!")
	
	    
	if (self.trainTestFlag == False):
	    if (self.detectFile != None):
		self.detectData()
	    else:
		print "Detection failed cause of a missing detection file!"
    
    def getIndexFromTo(self):
	selD = self.selectedData;
	trialnum = int(self.dataLength)
	window = 0.2 * trialnum

	index = Object()
	if (self.sameFile == True):
	    if(selD["All"] == True):
		start = 0
		end = trialnum
		
	    elif(selD["off0"] == True):
		start = 0
		end = trialnum
		#start = 0
		#end = window
	    elif(selD["off1"] == True):
		start = 0
		end = trialnum
		#start = 0.2 * trialnum
		#end = start + window
	    elif(selD["off2"] == True):
		start = 0
		end = trialnum
		#start = 0.4 * trialnum
		#end = start + window
	    elif(selD["off3"] == True):
		start = 0
		end = trialnum
		#start = 0.6 * trialnum
		#end = start + window
	    elif(selD["off4"] == True):
		start = 0
		end = trialnum
		#start = 0.8 * trialnum
		#end = trialnum #forced in case we have a missing final trial
	    else:
		#that could be implemented as an exception: check
		#and we could even make an asserting function to detect any unexpected behavior
		print "ops, offset checkbox isn't selected for detection from the samefile"
		start = -1
		end = -1
	else:
	    #take the whole file in case its a new one
	    start = 0
	    end = trialnum

	index.start = int(start)
	index.end = int(end)

	return index
    
    def detectData(self):
	cf = self.classifierFile
	self.setPreProjectedFlag()

	self.classifierResult = []
	self.realClasses = []
	
	

	if (self.sameFile):
	    #print a convenient detection path to avoid the user getting confused
	    #if he has a selection of a different path even while selecting the sameFile checkbox
	    convDetectPath = self.path
	else:
	    convDetectPath = self.detectFile

	#we may be later interested in providing a feedback for the signal start and end too! but for now, that's definitely not!
	detectionDescription = "Train = " + (self.path).split("/")[-1] + "\r\nNoise Removal = " + str(self.removeNoiseFlag)+ "\r\nSame File" + str(self.sameFile) + "\r\nDetect" + convDetectPath.split("/")[-1] + \
	"\r\nExtraction Flags = " + str(self.f1FLag) + str(self.f3FLag) + str(self.f4FLag) + str(self.f5FLag) + str(self.f6FLag) + \
	"\r\nPreprocessing Flags = " + str(self.NoneFilterFlag) + str(self.idealFlag) +str(self.butterFlag)+ "\r\nEnhancement flags " + str(self.NoneFlag)+ str(self.PCAFlag) +   str(self.LDAFlag) + "\r\nClassifier " + str(cf)
#str(self.CSP_LDAFlag) +
	indexWindow = 0

	if (cf == "KNN"):
	    trials = self.captureTrialData()
	    index = trials["index"]
	    indexWindow = index.end - index.start
	    self.knnResultInput["TrainOut"] =  self.knnTrainOut

	    for i in range (indexWindow):

		if (self.sameFile == True):
		    trial = trials["trials"][i]
		elif (self.sameFile == False):
		    trial = trials["trials"][:,:,i]

		self.knnResultInput["TrialData"] = trial
		self.knnResult = self.octave.feval('KNN_Generic_Detect.m',self.knnResultInput,  self.dataFile, self.removeNoiseFlag, self.idealFlag,     	self.butterFlag,self.NoneFilterFlag,self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag, self.preProjectedFlag)
		if (self.verbose):
		    feedback = "trial " + str(i) + ": PCA " + str(self.knnResult.PCAresult) + ", None " + str(self.knnResult.Noneresult) + ", LDA " + str(self.knnResult.LDAresult)
		    print feedback

		if (self.PCAFlag == 1):
		    self.classifierResult.append(self.knnResult.PCAResultClass)
		    
		elif (self.LDAFlag == 1):
		    self.classifierResult.append(self.knnResult.LDAResultClass)
		elif (self.NoneFlag == 1):
		    self.classifierResult.append(self.knnResult.NoneResultClass)
		
		if((self.sameFile==1) and (self.LDAFlag ==1)):
		    self.realClasses = self.knnTrainOut.ClassesTypesSameFile
		else:
		    self.realClasses = self.knnTrainOut.ClassesTypes

	    if (self.sameFile == False):
		self.realClasses = self.octave.feval('getRealClass.m', self.detectFile)
	    #print(self.realClasses)

	elif (cf == "Fisher"):
	    trials = self.captureTrialData()
	    index = trials["index"]
	    indexWindow = index.end - index.start
	    self.fisherResultInput["TrainOut"] =  self.fisherTrainOut

	    for i in range (indexWindow):

		if (self.sameFile == True):
		    # this condition implies wer had a preprocessed data ie: 1x28 trials
		    trial = trials["trials"][i]
		elif (self.sameFile == False):
		    # this conditio implies we had a raw data ie: 14x512 channelsXsamples
		    trial = trials["trials"][:,:,i]
		
		self.fisherResultInput["TrialData"] = trial
		self.fisherResult = self.octave.feval('Fisher_Generic_Detect.m',self.fisherResultInput,  self.dataFile, self.removeNoiseFlag, self.idealFlag, self.butterFlag,self.NoneFilterFlag,self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag, self.preProjectedFlag)
		if (self.verbose):
		    feedback = "trial " + str(i) + ": PCA " + str(self.fisherResult.PCAresult) + ", LDA " + str(self.fisherResult.LDAresult)
		    print feedback
		    print self.fisherResult.Z

		#TODO move into a separate function
		if (self.PCAFlag == 1):
		    self.classifierResult.append(self.fisherResult.PCAResultClass)
		elif (self.LDAFlag == 1):
		    self.classifierResult.append(self.fisherResult.LDAResultClass)

		self.realClasses = self.fisherTrainOut.ClassesTypes

	elif (cf == "Likelihood"):
	    trials = self.captureTrialData()
	    index = trials["index"]
	    indexWindow = index.end - index.start
	    self.likelihoodResultInput["TrainOut"] =  self.likelihoodTrainOut

	    for i in range (indexWindow):

		if (self.sameFile == True):
		    trial = trials["trials"][i]
		elif (self.sameFile == False):
		    trial = trials["trials"][:,:,i]

		self.likelihoodResultInput["TrialData"] = trial
		self.likelihoodResult = self.octave.feval('Likelihood_Generic_Detect.m',self.likelihoodResultInput,self.likelihoodClass,  self.dataFile, self.removeNoiseFlag, self.idealFlag, self.butterFlag,self.NoneFilterFlag,self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag, self.preProjectedFlag)
		if (self.verbose):
		    feedback = "trial " + str(i) + ": PCA " + str(self.likelihoodResult.PCAresult) + ", LDA " + str(self.likelihoodResult.LDAresult) + ", None " + str(self.likelihoodResult.Noneresult)
		    print feedback
		    #print self.likelihoodResult.vote
		    


		if (self.PCAFlag == 1):
		    self.classifierResult.append(self.likelihoodResult.PCAResultClass)
		    
		elif (self.LDAFlag == 1):
		    self.classifierResult.append(self.likelihoodResult.LDAResultClass)
		
		elif (self.NoneFlag == 1):
		    self.classifierResult.append(self.likelihoodResult.NoneResultClass)
		
		if((self.sameFile==1) and ((self.LDAFlag ==1) or (self.PCAFlag ==1)  )):
		    self.realClasses = self.likelihoodTrainOut.ClassesTypesSameFile
		else:
	    	    self.realClasses = self.likelihoodTrainOut.ClassesTypes
	   
	    if (self.sameFile == False):
		self.realClasses = self.octave.feval('getRealClass.m', self.detectFile)
	    print self.realClasses

	elif (cf == "Least Squares"):
	    trials = self.captureTrialData()
	    index = trials["index"]
	    indexWindow = index.end - index.start
	    self.leastSquaresResultInput["TrainOut"] =  self.leastSquaresTrainOut
	    
	    
	    for i in range (indexWindow):

		if (self.sameFile == True):
		    trial = trials["trials"][i]
		elif (self.sameFile == False):
		    trial = trials["trials"][:,:,i]
		   

		self.leastSquaresResultInput["TrialData"] = trial
		self.leastSquaresResult = self.octave.feval('Leastsquares_Generic_Detect.m',self.leastSquaresResultInput,  self.dataFile, self.removeNoiseFlag,self.idealFlag, self.butterFlag,self.NoneFilterFlag, self.f1FLag,self.f2FLag,self.f3FLag,self.f4FLag,self.f5FLag,self.f6FLag,self.LDAFlag,self.PCAFlag,self.CSP_LDAFlag,self.NoneFlag, self.preProjectedFlag)
		if (self.verbose):
		    feedback = "trial " + str(i) + ": PCA " + str(self.leastSquaresResult.PCAresult) + ", LDA " + str(self.leastSquaresResult.LDAresult) + ", None " + str(self.leastSquaresResult.NoneResult) 
		    print feedback

		if (self.PCAFlag == 1):
		    self.classifierResult.append(self.leastSquaresResult.PCAResultClass)
		elif (self.LDAFlag == 1):
		    self.classifierResult.append(self.leastSquaresResult.LDAResultClass)
		elif (self.NoneFlag == 1):
		    self.classifierResult.append(self.leastSquaresResult.NoneResultClass)
	    
	    if (self.sameFile == True):
		self.realClasses = self.leastSquaresTrainOut.ClassesTypes
	    elif (self.sameFile == False):
		self.realClasses = self.octave.feval('getRealClass.m', self.detectFile)
		

	self.trialStatues(indexWindow)
	self.accSensitivity(indexWindow)
	
	if (self.verbose):
	    print self.comparisonResults
	accTest = AU()
	self.accTestResult = accTest.correctPercentAccuracy(self.comparisonResults, self.verbose)

	summary = detectionDescription + "\r\n" + str(self.accTestResult) + "\r\n"
	#print summary
	print color.BOLD + color.YELLOW + summary + color.END  + color.END

	truePos="True Positive: "+str(self.TP)
	falsePos="False Positive: "+str(self.FP)
        trueNeg="True Negative: "+str(self.TN)
	falseNeg="False Negative: "+str(self.FN)
	par="Paramters: "+ "\r\n" +truePos+ "\r\n" +falsePos+ "\r\n" +trueNeg+ "\r\n" + falseNeg
	print color.BOLD + color.GREEN + par + color.END  + color.END
	if(self.TP+self.FN != 0):
	  sensitivity=(self.TP*1.0/(self.TP+self.FN))*100.0
	  senStr= "Sensitivity (TP/TP+TF): "+str(sensitivity)+ "% \r\n"
	else:
	  senStr="Undefined"
	if(self.TN+self.FP != 0):
	  specifity=(self.TN*1.0/(self.TN+self.FP))*100.0
	  specStr= "Specifity: (TN/TN+FP)"+str(specifity)+ "% \r\n"
	else:
	  specStr="Undefined"
	if(self.TP+self.FP != 0):
	  precision=(self.TP*1.0/(self.TP+self.FP))*100.0
	  precStr= "Precision (TP/TP+FP): "+str(precision)+ "% \r\n"
	else:
	  precStr="Undefined"

	#specifity=(self.TN*1.0/(self.TN+self.FP))*100.0
	#specStr= "Specifity: "+str(specifity)+ "% \r\n"
	#precision=(self.TP*1.0/(self.TP+self.FP))*100.0
	#precStr= "Precision: "+str(precision)+ "% \r\n"
	print color.BOLD + color.DARKCYAN + senStr + color.END  + color.END
	print color.BOLD + color.DARKCYAN + specStr + color.END  + color.END
	print color.BOLD + color.DARKCYAN + precStr + color.END  + color.END
	self.octave.close
	return self.accTestResult

	
    def getAcc(self):
	return self.accTestResult


    def accSensitivity(self,indexWindow):

	for i in range (indexWindow):
	    if (self.realClasses[i] == -1):
		self.realClasses[i] = 2
	    #print self.realClasses
	    #print self.classifierResult
	    
	    if (self.classifierResult[i] == 2 and int(self.realClasses[i])== 2 ):
		self.TN=self.TN+1
	    elif(self.classifierResult[i] ==1 and int(self.realClasses[i])== 1 ):
                self.TP=self.TP+1
	    elif(self.classifierResult[i] == 1 and int(self.realClasses[i])==2):
                self.FP=self.FP+1
	    elif(self.classifierResult[i] == 2 and int(self.realClasses[i])==1):
                self.FN=self.FN+1
 	    
	return self.TP,self.TN,self.FP,self.FN


    #for all the trials, compare and get the results into comparisonResults
    def trialStatues(self, indexWindow):

	self.comparisonResults = []

	for i in range (indexWindow):
	    if (self.realClasses[i] == -1):
		self.realClasses[i] = 2
	    #print self.realClasses
	    #print self.classifierResult
	    
	    if (self.classifierResult[i] == int(self.realClasses[i])):
		self.comparisonResults.append(True)

	    else:
		self.comparisonResults.append(False)	
	return self.comparisonResults

    def  captureTrialData(self):

	trials = {}
	if (self.sameFile == 1): 
	    index = self.getIndexFromTo()
	    if(self.LDAFlag == 1):

		## use the following to test the dimensions we get for each trial!
		## our first ref was 20x28
		#temp = self.LDAData[index.start:index.end]
		#print temp.shape
		trials["trials"] = self.LDAData[index.start:index.end]
		trials["index"] = index

	    elif(self.PCAFlag == 1):

		#notice that giving an upper index higher than the available no of elements, would clamp to the the number of elements
		trials["trials"] = self.PCAData[index.start:index.end]
		trials["index"] = index
	    
	    elif(self.NoneFlag == 1):
		trials["trials"] = self.NoneData[index.start:index.end]
		trials["index"] = index

	    return trials

	elif (self.sameFile == 0):
	    #read data from self.detectFile
	    #set trialnum
	    #TODO change 0 and 4 to the sampleStart and sampleEnd
	    octTrials = self.octave.feval('getTrialsData.m', self.detectFile, 0, 4)

	    self.dataLength = int(octTrials.shape[2])
	    #another way would be by adding a size attr to octTrials from getTrialsData.m ie:
	    #self.dataLength = int(octTrials)

	    # for debugging purposes use the following line ^_^
	    #print octTrials[:,:,3].shape

	    trials["trials"] = octTrials #the trials data itself need to feval getMuBeta functions
	    trials["index"] = self.getIndexFromTo()

	    return trials

    def setPreProjectedFlag(self):
	if (self.sameFile):
	    self.preProjectedFlag = 1
	else:
	    self.preProjectedFlag = 0

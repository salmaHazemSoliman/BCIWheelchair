function [mu,Beta] = NoFilter(data,operation = @mean,fs = 128,Mu_Min = 10,Mu_Max = 12,Beta_Min = 16,Beta_Max = 24)
    
    ChannelsNo  = size(data)(1);
    samplesNo   = size(data)(2);
    
    mu = zeros(1,ChannelsNo);
    Beta = zeros(1,ChannelsNo);

    freq = linspace(0,fs,samplesNo);

    for l = 1:ChannelsNo
         tempData = data(l,:);
         Data_freq = fft(tempData);
         Mu_freq_temp = Data_freq;
         Beta_freq_temp = Data_freq;         
         mu(1,l)    =  operation(abs(Mu_freq_temp)/length(Mu_freq_temp));
         Beta(1,l)  =  operation(abs(Beta_freq_temp)/length(Beta_freq_temp));
    end
       
end
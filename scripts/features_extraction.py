import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import librosa

class Extract: 
    def __init__(self):
        """
        Initializes the features_extraction object.
        """
        self.mfcc1 = 0
        self.mfcc2 = 0
        self.mfcc3 = 0
        self.mfcc4 = 0
        self.mfcc5 = 0
        self.mfcc6 = 0
        self.mfcc7 = 0
        self.mfcc8 = 0
        self.mfcc9 = 0
        self.mfcc10 = 0
        self.mfcc11 = 0
        self.mfcc12 = 0
        self.mfcc13 = 0
        self.zcr = 0
        self.centroid = 0
        self.RMSE = 0
        self.aud = None



    def load_audio(self, audio_path):
        """
        loading audio from a selcted path.
        """
        self.aud, sr = librosa.load(audio_path, sr = 16000)
        return self.aud

    def extract_features_lib(self, nfft, hop):
        """
        Extracting audio features.
        """
        #MFCC - 13 features per audio file
                
        mean_mfcc = np.mean(librosa.feature.mfcc(y=self.aud, sr=16000, n_mfcc=13, n_fft=nfft, hop_length=hop, window = 'hann').T,axis=0)
        
        #zero crossing rate - 1 feature per audio file  (averaging top 10% of ZCR over the whole file)
        zcr = librosa.feature.zero_crossing_rate(self.aud, frame_length=nfft, hop_length=hop)
        zcr_n=np.sort(zcr)[::-1]
        p = zcr.shape[1]
        lent = int(0.1*zcr.shape[1])
        zcr_10 = zcr_n[0,(p-lent):]
        avg_zcr = np.mean(zcr_10)
        
        #Spectral centroid - 1 feature per audio file
        avg_centroid = np.mean(librosa.feature.spectral_centroid(y=self.aud, sr=16000, n_fft=nfft, hop_length=hop, window='hann', center=True, pad_mode='reflect'))
        
        #RMS energy - 1 feature per audio file
        avg_RMSE = np.mean(librosa.feature.rms(y=self.aud, frame_length=nfft, hop_length=hop, center=True, pad_mode= 'reflect'))
        
        self.mfcc1 = mean_mfcc[0]
        self.mfcc2 = mean_mfcc[1]
        self.mfcc3 = mean_mfcc[2]
        self.mfcc4 = mean_mfcc[3]
        self.mfcc5 = mean_mfcc[4]
        self.mfcc6 = mean_mfcc[5]
        self.mfcc7 = mean_mfcc[6]
        self.mfcc8 = mean_mfcc[7]
        self.mfcc9 = mean_mfcc[8]
        self.mfcc10 = mean_mfcc[9]
        self.mfcc11 = mean_mfcc[10]
        self.mfcc12 = mean_mfcc[11]
        self.mfcc13 = mean_mfcc[12]
        # ZCR
        self.zcr = avg_zcr
                
        #Centroid
        self.centroid = avg_centroid
                
        #RMSE
        self.RMSE = avg_RMSE
        
    def to_csv(self):
        """
        Exporting features in CSV file.
        """
        df = pd.DataFrame(np.column_stack([self.mfcc1, self.mfcc2, self.mfcc3, self.mfcc4, self.mfcc5, self.mfcc6, self.mfcc7, self.mfcc8, self.mfcc9, self.mfcc10, self.mfcc11, self.mfcc12, self.mfcc13, self.zcr, self.centroid, self.RMSE]), 
                               columns=['mean_mfcc1', 'mean_mfcc2', 'mean_mfcc3', 'mean_mfcc4', 'mean_mfcc5', 'mean_mfcc6', 'mean_mfcc7', 'mean_mfcc8', 'mean_mfcc9', 'mean_mfcc10', 'mean_mfcc11', 'mean_mfcc12', 'mean_mfcc13', 'mean_zcr', 'mean_centroid', 'mean_RMSE'])

        label = 1 #1 for scream 
        df['label'] = label
        #save new data in excel file
        df.to_csv("../csv/runtime.csv", index = False)
    
    def extraction(self, file):
        self.load_audio(file)
        self.extract_features_lib(512, 256) #audio, frame length and hop length
        self.to_csv()




    








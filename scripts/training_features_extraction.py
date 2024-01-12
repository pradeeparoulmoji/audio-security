import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import librosa


# create features lists to put the results

mfcc1 = []
mfcc2 = []
mfcc3 = []
mfcc4 = []
mfcc5 = []
mfcc6 = []
mfcc7 = []
mfcc8 = []
mfcc9 = []
mfcc10 = []
mfcc11 = []
mfcc12 = []
mfcc13 = []
zcr = []
centroid = []
RMSE = []

#starting from 0 files
i = 0

Directory_scream = "../training_audio_files/scream"   #Directory where the files live
Directory_bg = "../training_audio_files/not_scream"    #Directory where the files live
file_list_scream = os.listdir(Directory_scream)
file_list_bg = os.listdir(Directory_bg)

#Extract librosa features in a function

def extract_features_lib(aud, nfft, hop):
    #MFCC - 13 features per audio file
    
    mean_mfcc = np.mean(librosa.feature.mfcc(y=aud, sr=16000, n_mfcc=13, n_fft=nfft, hop_length=hop, window = 'hann').T,axis=0)
    
    #zero crossing rate - 1 feature per audio file  (averaging top 10% of ZCR over the whole file)
    zcr = librosa.feature.zero_crossing_rate(aud, frame_length=nfft, hop_length=hop)
    zcr_n=np.sort(zcr)[::-1]
    p = zcr.shape[1]
    lent = int(0.1*zcr.shape[1])
    zcr_10 = zcr_n[0,(p-lent):]
    avg_zcr = np.mean(zcr_10)
    
    #Spectral centroid - 1 feature per audio file
    avg_centroid = np.mean(librosa.feature.spectral_centroid(y=aud, sr=16000, n_fft=nfft, hop_length=hop, window='hann', center=True, pad_mode='reflect'))
    
    #RMS energy - 1 feature per audio file
    avg_RMSE = np.mean(librosa.feature.rms(y=aud, frame_length=nfft, hop_length=hop, center=True, pad_mode= 'reflect'))
    return mean_mfcc, avg_zcr, avg_centroid, avg_RMSE

#Feature Extraction starts for 0 file in the file_list_scream

i=0

for filename in file_list_scream:
    aud, sr = librosa.load(Directory_scream + '/'+ file_list_scream[i], sr = 16000)
    
    # Get audio and apply feature extraction
    (mean_mfcc, avg_zcr, avg_centroid, avg_RMSE) = extract_features_lib(aud, 512, 256) #audio, frame length and hop length
    #Store the extracted features
    # MFCC (1-13)
    mfcc1.append(mean_mfcc[0])
    mfcc2.append(mean_mfcc[1])
    mfcc3.append(mean_mfcc[2])
    mfcc4.append(mean_mfcc[3])
    mfcc5.append(mean_mfcc[4])
    mfcc6.append(mean_mfcc[5])
    mfcc7.append(mean_mfcc[6])
    mfcc8.append(mean_mfcc[7])
    mfcc9.append(mean_mfcc[8])
    mfcc10.append(mean_mfcc[9])
    mfcc11.append(mean_mfcc[10])
    mfcc12.append(mean_mfcc[11])
    mfcc13.append(mean_mfcc[12])

    # ZCR
    zcr.append(avg_zcr)
    
    #Centroid
    centroid.append(avg_centroid)
    
    #RMSE
    RMSE.append(avg_RMSE)
    
    i+=1   #Go to next file in the file_list

#save data in pandas dataframe
df = pd.DataFrame(np.column_stack([mfcc1, mfcc2, mfcc3, mfcc4, mfcc5, mfcc6, mfcc7, mfcc8, mfcc9, mfcc10, mfcc11, mfcc12, mfcc13, zcr, centroid, RMSE]), 
                               columns=['mean_mfcc1', 'mean_mfcc2', 'mean_mfcc3', 'mean_mfcc4', 'mean_mfcc5', 'mean_mfcc6', 'mean_mfcc7', 'mean_mfcc8', 'mean_mfcc9', 'mean_mfcc10', 'mean_mfcc11', 'mean_mfcc12', 'mean_mfcc13', 'mean_zcr', 'mean_centroid', 'mean_RMSE'])

label = 1 #1 for scream
df['label'] = label
#save new data in excel file
df.to_csv("../csv/scream.csv", index = False)

print("Done!") 

# create lists to put the results

mfcc1 = []
mfcc2 = []
mfcc3 = []
mfcc4 = []
mfcc5 = []
mfcc6 = []
mfcc7 = []
mfcc8 = []
mfcc9 = []
mfcc10 = []
mfcc11 = []
mfcc12 = []
mfcc13 = []
zcr = []
centroid = []
RMSE = []

#Feature Extraction starts for 0 file in the file_list_bg

i=0
for filename in file_list_bg:
    aud, sr = librosa.load(Directory_bg + '/'+ file_list_bg[i], sr = 16000)
    
    # Get audio and apply feature extraction
    (mean_mfcc, avg_zcr, avg_centroid, avg_RMSE) = extract_features_lib(aud, 512, 256) #audio, frame length and hop length
    #Store the extracted features
    # MFCC (1-13)
    mfcc1.append(mean_mfcc[0])
    mfcc2.append(mean_mfcc[1])
    mfcc3.append(mean_mfcc[2])
    mfcc4.append(mean_mfcc[3])
    mfcc5.append(mean_mfcc[4])
    mfcc6.append(mean_mfcc[5])
    mfcc7.append(mean_mfcc[6])
    mfcc8.append(mean_mfcc[7])
    mfcc9.append(mean_mfcc[8])
    mfcc10.append(mean_mfcc[9])
    mfcc11.append(mean_mfcc[10])
    mfcc12.append(mean_mfcc[11])
    mfcc13.append(mean_mfcc[12])

    # ZCR
    zcr.append(avg_zcr)
    
    #Centroid
    centroid.append(avg_centroid)
    
    #RMSE
    RMSE.append(avg_RMSE)
    
    i+=1   #Go to next file in the file_list

#save data in pandas dataframe
df = pd.DataFrame(np.column_stack([mfcc1, mfcc2, mfcc3, mfcc4, mfcc5, mfcc6, mfcc7, mfcc8, mfcc9, mfcc10, mfcc11, mfcc12, mfcc13, zcr, centroid, RMSE]), 
                               columns=['mean_mfcc1', 'mean_mfcc2', 'mean_mfcc3', 'mean_mfcc4', 'mean_mfcc5', 'mean_mfcc6', 'mean_mfcc7', 'mean_mfcc8', 'mean_mfcc9', 'mean_mfcc10', 'mean_mfcc11', 'mean_mfcc12', 'mean_mfcc13', 'mean_zcr', 'mean_centroid', 'mean_RMSE'])

label = 0 #0 for non-scream
df['label'] = label
#save new data in excel file
df.to_csv("../csv/not_scream.csv", index = False)

print("Done!") 


# Load the two CSV files
df1 = pd.read_csv("../csv/scream.csv")
df2 = pd.read_csv("../csv/not_scream.csv")

# Delete the first row of df2
df2 = df2.drop(df2.index[0])

# Concatenate the two dataframes
df = pd.concat([df1, df2])

# Save the combined dataframe to a new CSV file
df.to_csv("../csv/training_dataset.csv", index=False)
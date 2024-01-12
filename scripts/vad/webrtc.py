import struct 
import librosa # librosa==0.9.1
import webrtcvad # webrtcvad==2.0.10
import numpy as np
import pandas as pd

# load data
file_path = 'C:/Users/tm2378/Documents/GitHub/audio-security/audio_files/effected/effected.wav'


# load wav file (librosa)
y, sr = librosa.load(file_path, sr=16000)
# convert the file to int if it is in float (Py-WebRTC requirement)
if y.dtype.kind == 'f':
    # convert to int16
    y = np.array([ int(s*32768) for s in y])
    # bound
    y[y > 32767] = 32767
    y[y < -32768] = -32768

# create raw sample in bit
raw_samples = struct.pack("%dh" % len(y), *y) #into a binary data string 

# define webrtcvad VAD
vad = webrtcvad.Vad(0) # set aggressiveness from 0 to 3
window_duration = 0.03 # duration in seconds
samples_per_window = int(window_duration * sr + 0.5) #approx 480
bytes_per_sample = 2 # for int16

# Start classifying chunks of samples
# var to hold segment wise report
segments = []
# iterate over the audio samples
# Iterate over windows of the audio data
max = 0 #chunks to process in order to dont have error
for i, start in enumerate(np.arange(0, len(y)-481, samples_per_window)): #-481 in order to dont have error(16000 hz)
    # Determine the stop index for the current window
    stop = min(start + samples_per_window, len(y))
    
    # Extract the raw audio sample data for the current window
    loc_raw_sample = raw_samples[start * bytes_per_sample: stop * bytes_per_sample]

   
 
    try:
        # Use VAD to check if the current window contains speech
        is_speech = vad.is_speech(loc_raw_sample, sample_rate=16000)
        
        # Append information about the current segment to the 'segments' list
        segments.append(dict(
            start=start,
            stop=stop,
            is_speech=is_speech,
            time=0.03*i
        ))
    except Exception as e:
        # Handle exceptions, print an error message
        print(f"Failed for step {i}, reason: {e}")

df = pd.DataFrame(segments) # result of classification
excel_file_path = 'output2.xlsx'

# Export the DataFrame to Excel
df.to_excel(excel_file_path, index=False)

print(df)


#nel main if ce voce and maggiore di una soglia tieni il file
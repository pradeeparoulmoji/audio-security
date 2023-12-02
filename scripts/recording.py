import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import threading
import time

class Recording:
    def __init__(self):
        self.duration = 10   # total desired duration of recording
        self.fs = 44100      # deafult sample rate
        self.recording = []  # list of chunk recordings
        self.split = 2       # total duration of each chunk recording


    # Record audio
    def record(self):
       
     for i in range(int(self.duration/self.split)): # number of chunks
        output_file = f"stereo_audio3{i}.wav"    # for each itearation, create a new file name
        self.recording.append(sd.rec(int(self.split * self.fs), samplerate=self.fs, channels=2)) # record i-th chunk
        sd.wait()
        scaled_audio_data = np.int16(self.recording[i] * 32767) # Scale the audio data to the appropriate range for 16-bit PCM (typically -32768 to 32767)
        write(output_file, self.fs, scaled_audio_data) # Save the chunk data as a WAV file
        
    





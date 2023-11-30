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
         self.recording.append(sd.rec(int(self.split * self.fs), samplerate=self.fs, channels=2))
        
        # Wait for the recording to finish
         sd.wait()
        
        return self.recording

    def write(self):
        for i in range(len(self.recording)):
            
            output_file = f"stereo_audio{i}.wav" 
            # Scale the audio data to the appropriate range for 16-bit PCM (typically -32768 to 32767)
            scaled_audio_data = np.int16(self.recording[i] * 32767)
            # Save the audio data as a WAV file
            write(output_file, self.fs, scaled_audio_data)

    
a = Recording()
print(len(a.record()))
a.write()



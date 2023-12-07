import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import threading
import time


class Recording:
    

    def __init__(self):
        """
        Initializes a Recording object.

        Attributes:
        - duration: int, total desired duration of recording
        - fs: int, default sample rate
        - recording: list, list of chunk recordings
        - split: int, total duration of each chunk recording
        """
        self.duration = 60  # total desired duration of recording
        self.fs = 44100      # deafult sample rate
        self.recordings = []  # list of chunk recordings
        self.split = 10       # total duration of each chunk recording

    def record(self):
        """
        Record audio and return the queue file paths in order to use them in the main script.
        
        Returns:
            None
        
        """
        for i in range(int(self.duration/self.split)): # for every chunk
            output_file = f"../audio_files/source/source{i}.wav"    # for each iteration, create a new file name
            self.recordings.append(sd.rec(int(self.split * self.fs), samplerate=self.fs, channels=2)) # record i-th chunk
            sd.wait() #wait until recording is finished
            scaled_audio_data = np.int16(self.recordings[i] * 32767) # Scale the audio data to the appropriate range for 16-bit PCM (typically -32768 to 32767)
            write(output_file, self.fs, scaled_audio_data) # Save the chunk data as a WAV file









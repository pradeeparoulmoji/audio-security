import noisereduce as nr
from scipy.io import wavfile
import matplotlib.pyplot as plt
from pedalboard.io import AudioFile
from pedalboard import *
import librosa
import numpy as np


#prossimo obbiettivo nel preprossecing: variabili che cambiano in base alla sorgente


class PreProcessing: 
    def __init__(self, file_path, path_dest, target_sr=44100): #inizializzazione
        self.file_path = file_path
        self.file_path_dest = path_dest
        self.target_sr = target_sr
        self.duration = 0
        self.samplerate = 0
        self.num_channels = 0
        self.low_freq = 400
        self.high_freq = 3500
        self.noise_gate_thres = -26
        self.audio_frames = None

    def read_audio(self,path): #read audio file with pedalboard library
        with AudioFile(path).resampled_to(self.target_sr) as f:
            self.duration = f.duration
            self.samplerate = self.target_sr
            self.num_channels = f.num_channels
            self.audio_frames = f.read(int(self.samplerate * (self.duration))) #creating all the audio frames

    def plot_audio_channels(self): #plotting both audio channels 
        duration = int(self.duration)
        sample_rate = self.target_sr
        time = np.linspace(0, self.duration, num=int(self.samplerate * (self.duration)))
        audio_data = self.audio_frames
        #audio_data_dB = 20 * np.log10(audio_data) #optional
        

        plt.figure(figsize=(14, 5))
        

        for i in range(self.num_channels): #grafico per ogni chanel
            plt.subplot(self.num_channels, 1, i + 1)
            plt.plot(time, audio_data[i])
            plt.title(f'Channel {i + 1}')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')

        plt.tight_layout()
        plt.show()
        

    def process_audio(self):
        board = Pedalboard([Gain(gain_db=20)])
        reduced_noise = nr.reduce_noise(y=self.audio_frames, sr=self.target_sr, stationary=True, prop_decrease=0.9)
        board.append(HighShelfFilter(cutoff_frequency_hz= self.high_freq,gain_db=-30))
        board.append(LowShelfFilter(cutoff_frequency_hz= self.low_freq,gain_db=-30))
        board.append(NoiseGate(threshold_db= self.noise_gate_thres, release_ms=2000))

                 
        
        
        effected = board(reduced_noise, self.target_sr)

        


        with AudioFile(self.file_path_dest, 'w', self.target_sr, effected.shape[0]) as f:
         f.write(effected)


    
  


file_path = "C:/Users/tm2378/Desktop/TIROCINIO/WAV/221163__caquet__street-traffic-a-cafeteria-and-some-noisy-birds.wav"
file_path_dest = 'C:/Users/tm2378/Desktop/TIROCINIO/WAV/effected90.wav'
processor = PreProcessing(file_path, file_path_dest)
processor.read_audio(file_path)

processor.process_audio()
processor.plot_audio_channels() #original audio plot

processor.read_audio(file_path_dest)
processor.plot_audio_channels() #processed audio plot

print("finished")
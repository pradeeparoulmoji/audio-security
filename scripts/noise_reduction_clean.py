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
    def __init__(self, file_path, path_dest, target_sr=44100):  # Initialization method
    # Store the input parameters as attributes of the object
        self.file_path = file_path       # Path to the input audio file
        self.file_path_dest = path_dest  # Path to the destination file
        self.target_sr = target_sr       # Target sample rate for processing
        self.duration = 0                # Initialize duration attribute (to be updated later)
        self.samplerate = 0              # Initialize sample rate attribute (to be updated later)
        self.num_channels = 0            # Initialize number of channels attribute (to be updated later)
        self.low_freq = 400              # Default low-frequency cutoff for processing
        self.high_freq = 3500            # Default high-frequency cutoff for processing
        self.noise_gate_thres = -26      # Default noise gate threshold
        self.audio_frames = None         # Placeholder for audio frames (to be populated later)
        self.audio_noise_frames = None   # Placeholder for audio frames containing noise (to be populated later)


    

    def read_audio(self, path, noise):
        # Read the main audio file using the pedalboard library
        with AudioFile(path).resampled_to(self.target_sr) as f:
            # Update duration, sample rate, and number of channels attributes
            self.duration = f.duration
            self.samplerate = self.target_sr
            self.num_channels = f.num_channels
            self.audio_frames = f.read(int(self.samplerate * (self.duration))) #creating all the audio frames
            # Create audio frames by reading the entire audio file
            self.audio_frames = f.read(int(self.samplerate * self.duration))

        # Read the noise audio file using the pedalboard library
        with AudioFile(noise).resampled_to(self.target_sr) as n:
            # Create noise audio frames by reading the entire noise audio file
            self.audio_noise_frames = n.read(int(self.target_sr * n.duration))
                

    def plot_audio_channels(self): #plotting both audio channels 
    def plot_audio_channels(self):
        # Extract necessary information for plotting
        duration = int(self.duration)
        sample_rate = self.target_sr
        time = np.linspace(0, self.duration, num=int(self.samplerate * (self.duration)))
        time = np.linspace(0, self.duration, num=int(self.samplerate * self.duration))
        audio_data = self.audio_frames
        #audio_data_dB = 20 * np.log10(audio_data) #optional
        
        # audio_data_dB = 20 * np.log10(audio_data)  # Optional (commented out)

        # Set up the plot
        plt.figure(figsize=(14, 5))
        

        for i in range(self.num_channels): #grafico per ogni chanel
        # Plot each audio channel
        for i in range(self.num_channels):
            plt.subplot(self.num_channels, 1, i + 1)
            plt.plot(time, audio_data[i])
            plt.title(f'Channel {i + 1}')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')

        # Adjust layout and display the plot
        plt.tight_layout()
        plt.show()

    def noise_gate_setup(self,audio): #set (max amplitude+avg)/2
        
        audio_data = audio

        # Find the maximum absolute amplitude
        max_amplitude = np.max(np.abs(audio_data))
        # Calculate average amplitude
        average_amplitude = np.mean(np.abs(audio_data))
        max_amplitude_db_mean = 20 * np.log10(max_amplitude)
        average_amplitude_db_mean = 20 * np.log10(average_amplitude)
        return (max_amplitude_db_mean+average_amplitude_db_mean)/1.75

    def process_audio(self):
        # Create a Pedalboard with a Gain effect
        board = Pedalboard([Gain(gain_db=20)])
        reduced_noise = nr.reduce_noise(y=self.audio_frames, sr=self.target_sr, stationary=True, prop_decrease=0.9)
        board.append(HighShelfFilter(cutoff_frequency_hz= self.high_freq,gain_db=-30))
        board.append(LowShelfFilter(cutoff_frequency_hz= self.low_freq,gain_db=-30))
        board.append(NoiseGate(threshold_db= self.noise_gate_thres, release_ms=2000))

                 
        
        
        # Reduce noise using the reduce_noise function from the noisereduce library
        reduced_noise = nr.reduce_noise(y=self.audio_frames, sr=self.target_sr, stationary=True, prop_decrease=0.9, n_fft=512)
        reduced_noise = nr.reduce_noise(y=reduced_noise, sr=self.target_sr, y_noise=self.audio_noise_frames, stationary=False, prop_decrease=0.5, n_fft=512)

        # Append HighShelfFilter and LowShelfFilter effects to the Pedalboard
        board.append(HighShelfFilter(cutoff_frequency_hz=self.high_freq, gain_db=-30))
        board.append(LowShelfFilter(cutoff_frequency_hz=self.low_freq, gain_db=-30))

        # Apply the effects to the audio signal
        effected = board(reduced_noise, self.target_sr)

        
        # Set up the noise gate using the noise_gate_setup method
        self.noise_gate_thres = self.noise_gate_setup(effected)
        board.append(NoiseGate(threshold_db=self.noise_gate_thres, release_ms=2000))

        # Apply the effects again after adding the noise gate
        effected = board(reduced_noise, self.target_sr)

        # Write the processed audio to the destination file
        with AudioFile(self.file_path_dest, 'w', self.target_sr, effected.shape[0]) as f:
         f.write(effected)
            f.write(effected)


        


        


    
  


file_path = "C:/Users/tm2378/Desktop/TIROCINIO/WAV/221163__caquet__street-traffic-a-cafeteria-and-some-noisy-birds.wav"
file_path_dest = 'C:/Users/tm2378/Desktop/TIROCINIO/WAV/effected90.wav'
file_path = "C:/Users/tm2378/Desktop/TIROCINIO/WAV/more2.wav"
file_path_noise = "C:/Users/tm2378/Desktop/TIROCINIO/WAV/noises.wav"
file_path_dest = 'C:/Users/tm2378/Desktop/TIROCINIO/WAV/effectedoooooooooooooo.wav'
processor = PreProcessing(file_path, file_path_dest)
processor.read_audio(file_path)
processor.read_audio(file_path,file_path_noise)

processor.process_audio()
processor.plot_audio_channels() #original audio plot
#processor.plot_audio_channels() #original audio plot

#processor.read_audio(file_path_dest)
#processor.plot_audio_channels() #processed audio plot

processor.read_audio(file_path_dest)
processor.plot_audio_channels() #processed audio plot
print("finished")

print("finished")
#Note finali: ad ogni finestra matplotlib che si apre, per visualizzare la successiva bidsogna chiudere la precedente
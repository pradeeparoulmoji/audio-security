import noisereduce as nr
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pedalboard
from pedalboard.io import AudioFile
import librosa
import numpy as np




class PreProcessing: 
    def __init__(self, target_sr=44100):
        """
        Initializes the NoiseReductionClean object.

        Parameters:
        - target_sr (int): The target sample rate for processing. Default is 44100.
        """
        self.file_path_dest = None
        self.target_sr = target_sr
        self.duration = 0
        self.samplerate = 0
        self.num_channels = 0
        self.low_freq = 400
        self.high_freq = 3500
        self.noise_gate_thres = -26
        self.audio_frames = None
        self.audio_noise_frames = None


    

    def read_audio(self, path, noise):
        """
        Read the main audio file and the noise audio file.

        Args:
            path (str): The path to the main audio file.
            noise (str): The path to the noise audio file.

        Returns:
            None
        """
        # Read the main audio file using the pedalboard library
        with AudioFile(path).resampled_to(self.target_sr) as f:
            # Update duration, sample rate, and number of channels attributes
            self.duration = f.duration
            self.samplerate = self.target_sr
            self.num_channels = f.num_channels
            # Create audio frames by reading the entire audio file
            self.audio_frames = f.read(int(self.samplerate * self.duration))

        # Read the noise audio file using the pedalboard library
        with AudioFile(noise).resampled_to(self.target_sr) as n:
            # Create noise audio frames by reading the entire noise audio file
            self.audio_noise_frames = n.read(int(self.target_sr * n.duration))

    def plot_audio_channels(self):
        """
        Plot the audio channels.

        This method plots each audio channel separately on a single figure.
        Each channel is represented by its amplitude over time.

        Returns:
            None
        """
        # Extract necessary information for plotting
        time = np.linspace(0, self.duration, num=int(self.samplerate * self.duration))
        audio_data = self.audio_frames
        

        # Set up the plot
        plt.figure(figsize=(14, 5))

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

    def noise_gate_setup(self, audio):
        """
        Calculates the noise gate threshold for the given audio.

        Parameters:
        audio (ndarray): The audio data as a numpy array.

        Returns:
        float: The noise gate threshold.
        """
        audio_data = audio

        # Find the maximum absolute amplitude
        max_amplitude = np.max(np.abs(audio_data))
        # Calculate average amplitude
        average_amplitude = np.mean(np.abs(audio_data))
        max_amplitude_db_mean = 20 * np.log10(max_amplitude)
        average_amplitude_db_mean = 20 * np.log10(average_amplitude)
        return (max_amplitude_db_mean + average_amplitude_db_mean) / 1.75

    def process_audio(self, path_dest):
        """
        Process the audio by applying noise reduction and effects to the audio signal.

        Args:
            path_dest (str): The destination file path to save the processed audio.

        Returns:
            None
        """
        self.file_path_dest = path_dest
        # Create a Pedalboard with a Gain effect
        board = pedalboard.Pedalboard([pedalboard.Gain(gain_db=20)])

        # Reduce noise using the reduce_noise function from the noisereduce library
        reduced_noise = nr.reduce_noise(y=self.audio_frames, sr=self.target_sr, stationary=True, prop_decrease=0.9, n_fft=512)
        reduced_noise = nr.reduce_noise(y=reduced_noise, sr=self.target_sr, y_noise=self.audio_noise_frames, stationary=False, prop_decrease=0.5, n_fft=512)

        # Append HighShelfFilter and LowShelfFilter effects to the Pedalboard
        board.append(pedalboard.HighShelfFilter(cutoff_frequency_hz=self.high_freq, gain_db=-30))
        board.append(pedalboard.LowShelfFilter(cutoff_frequency_hz=self.low_freq, gain_db=-30))

        # Apply the effects to the audio signal
        effected = board(reduced_noise, self.target_sr)

        # Set up the noise gate using the noise_gate_setup method
        self.noise_gate_thres = self.noise_gate_setup(effected)
        board.append(pedalboard.NoiseGate(threshold_db=self.noise_gate_thres, release_ms=2000))

        # Apply the effects again after adding the noise gate
        effected = board(reduced_noise, self.target_sr)

        # Write the processed audio to the destination file
        with AudioFile(self.file_path_dest, 'w', self.target_sr, effected.shape[0]) as f:
            f.write(effected)


        


        


    
  


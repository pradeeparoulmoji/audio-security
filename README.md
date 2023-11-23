# audio-security
**Run the following command to install the required dependencies: pip install -r requirements.txt**


Audio-Security is an advanced Python project designed for enhancing security systems by implementing voice detection algorithms over security camera microphones. The primary goal of this project is to identify and analyze audio signals in real-time, allowing for the prompt detection of potential security threats or unauthorized access through voice recognition.

In our project, ensuring the clarity and accuracy of voice detection is crucial. To achieve this, we employ advanced noise cleaning techniques facilitated by key Python libraries.
To accomplish this, we depended on certain Python open-source libraries, which we will now elucidate:

**noisereduce**: a robust Python library designed to address the critical task of noise reduction in audio signals. It is capable of processing Stationary and Non-Stationary noise and to attenuate them.

**Pedalboard**: a Python library from Spotify for working with audio: reading, writing, rendering, adding effects, and more.

**matplotlib**: a Python library for plotting audio waveforms.

In the "scripts" directory, you will discover a file named "noise_reduction_clean.py," serving as the script employed for denoising our source audio files. Within the "audio_files" directory, two files are present: one, which goes by "source.wav" featuring the original source audio, while the other, which goes by "effected.wav" showcases the denoised version.





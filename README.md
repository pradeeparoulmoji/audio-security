# audio-security
**Run the following command to install the required dependencies: pip install -r requirements.txt**


Audio-Security is an advanced Python project designed for enhancing security systems by implementing voice detection algorithms over security camera microphones. The primary goal of this project is to identify and analyze audio signals in real-time, allowing for the prompt detection of potential security threats through voice recognition.

In our project, ensuring the clarity and accuracy of voice detection is crucial. To achieve this, we employ advanced noise cleaning techniques facilitated by key Python libraries.
To accomplish this, we depended on certain Python open-source libraries, which we will now elucidate:

**noisereduce**: a robust Python library designed to address the critical task of noise reduction in audio signals. It is capable of processing Stationary and Non-Stationary noise and to attenuate them.

**Pedalboard**: a Python library from Spotify for working with audio: reading, writing, rendering, adding effects, and more.

**matplotlib**: a Python library for plotting audio waveforms.

**sounddevice**: a Python interface for playing and recording sound

**scipy**: a Python library that allows to write wav files given numerical arrays.

In the "scripts" directory, you will discover a file named "noise_reduction_clean.py," serving as the script employed for denoising our source audio files. There is then a record.py which allows to record audio from a micrphone. The main scrpit takes all the scripts mentioned and puts them together. Within the "audio_files" directory, three folders are present: one, labeled "source" that contains segments of the audio recorded by the microphone, the second one, labeled "effected" contains the corresponding processed audio. The third one, labeled "noises," includes a sample of ambient noise that can be customized by the user according to their specific requirements.

The working process is captured in the following picture, offering a clear and efficient overview.
![Working process](https://github.com/pradeeparoulmoji/audio-security/blob/main/pictures/recording%20process.png)







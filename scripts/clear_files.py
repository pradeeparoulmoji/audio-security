import os
import glob

def delete_wav_files(directory):
    # Get a list of all .wav files in the directory
    wav_files = glob.glob(os.path.join(directory, '*.wav'))

    # Delete each file
    for file in wav_files:
        os.remove(file)

# Use the function
delete_wav_files('../audio_files/source/')
delete_wav_files('../audio_files/effected/')
delete_wav_files('../audio_files/source/detection')
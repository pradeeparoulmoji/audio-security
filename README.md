# audio-security
**In the scripts folder, Run the following command to install the required dependencies: pip install -r requirements.txt** \
**Run main_test.py to execute**


Audio-Security is an advanced Python project designed for enhancing security systems by implementing voice detection algorithms over security camera microphones. The primary goal of this project is to identify and analyze audio signals in real-time, allowing for the prompt detection of potential security threats through voice recognition.

In our project, ensuring the clarity and accuracy of voice detection is crucial. To achieve this, we employ advanced noise cleaning techniques facilitated by key Python libraries.
To accomplish this, we depended on certain Python open-source libraries.
We subsequently employed Support Vector Machines (SVM) to analyze audio signals captured by microphones.



In the "scripts" directory, you will discover a file named "noise_reduction_clean.py," serving as the script employed for denoising our source audio files. There is then a record.py which allows to record audio from a micrphone.

--The project is composed of multiple scripts:\
**main.py** is the script to execute in order to run the whole program 
**noise_reduction_clean** is the piece of code that performs the noise cleaning\
**recording.py** is the piece of code that performs the recording of audio from an input microphone.\
**model_svm.py** is the piece of code used to train our model\
**model_import.py** is the piece of code to correctly import the model into the main script.\
**features.extraction.py** is the piece of code that converts an audio file into a list of audio features\

--There are then some other minor scripts used to train our model and to mantain the whole project:\
**training_features_extraction.py** is a piece of code used to convert training audio files into a CSV file containing audio features from every file.\
**clear_files** is a simple script to delete all the directories before executing the main function



The main scrpit takes all the scripts mentioned and puts them together. Within the "audio_files" directory, three folders are present: one, labeled "source" that contains segments of the audio recorded by the microphone, the second one, labeled "effected" contains the corresponding processed audio. Inside of the "source" there is another folder named "detection" used to store every file that contains unusual sounds from the source files as screams.

--**running the main script**\
When the script is initiated, audio recording commences. Every two seconds, a new file is appended to the "source" folder. Subsequently, the audio file undergoes automatic denoising and is placed in the "effected" folder. The processed file is then fed into the SVM model. If the model detects a scream or any highly unusual sounds, "Scream detected + a timestamp" is outputted, and the associated source file chunk is relocated to the "detection" folder.

The working process is captured in the following picture, offering a clear and efficient overview.\
![Working process](https://github.com/pradeeparoulmoji/audio-security/blob/main/pictures/recording%20process.png)







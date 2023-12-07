import noise_reduction_clean
import recording
import threading
import time
import queue
import os


file_path_noise = "../audio_files/noises/noises.wav" # path to the noise file
finished = False # flag to indicate whether the recording is finished or not
total_duration = 20 # total duration of the recording
delay = 4 # chunk time (to be set in the record_audio() function)


def record_audio():
    """
    Records audio using the recording object.
    """
    rec = recording.Recording(total_duration,delay) # recording.py object
    rec.record() # recording.py method
    
    
    

def process_audio(): 
    """
    Process audio files by reading them, applying noise reduction, and saving the processed files.

    This function reads audio files from the '../audio_files/source' directory, applies noise reduction using the
    'noise_reduction_clean.PreProcessing' class, and saves the processed files to the '../audio_files/effected' directory.

    The function continues processing audio files until there are no more files in the '../audio_files/source' directory.

    Note: This function assumes that the 'noise_reduction_clean' module has been imported and the 'PreProcessing' class
    is available.

    Args:
        None

    Returns:
        None
    """
    processor = noise_reduction_clean.PreProcessing() # noise_reduction_clean.py
    i = 0 # counter
    
    while True:
        if i == 0:
            time.sleep(delay+1) # wait 
            if os.path.exists(f"../audio_files/source/source{i}.wav"):
                processor.read_audio(f"../audio_files/source/source{i}.wav", file_path_noise) # read the file
                processor.process_audio(f"../audio_files/effected/effected{i}.wav")     # process the file
            i = i + 1
        else:
            time.sleep(delay) # wait
            if os.path.exists(f"../audio_files/source/source{i}.wav"): # if the file exists
                processor.read_audio(f"../audio_files/source/source{i}.wav", file_path_noise) # read the file
                processor.process_audio(f"../audio_files/effected/effected{i}.wav") # process the file
                i = i + 1
            else:
                break # break the loop if the file does not exist

if __name__ == "__main__":
    # Create threads for the producer and the consumer
    producer_thread = threading.Thread(target=record_audio, daemon=True) #The daemon=True argument in the Thread constructor means that the threads will not prevent the program from exiting. When the main thread finishes, these daemon threads will also stop.
    consumer_thread = threading.Thread(target=process_audio, daemon=True)

    
    
    
    consumer_thread.start() # start the consumer thread
    producer_thread.start() # start the producer thread
    

    
    producer_thread.join() # join() method waits for the thread to complete its task
    consumer_thread.join() # join() method waits for the thread to complete its task

    print("Both threads have finished.")

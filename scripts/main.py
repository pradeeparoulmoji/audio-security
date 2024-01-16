import noise_reduction_clean
import features_extraction
import model_import
import recording
import threading
import time
import queue
import os
import shutil
from datetime import datetime




file_path_noise = "../audio_files/noises/noises.wav" # path to the noise file
finished = False # flag to indicate whether the recording is finished or not
total_duration = int(input("insert desired recording duration in seconds: ")) # total duration of the recording
delay = 2 # chunk time (to be set in the record_audio() function)


def record_audio():
    """
    Records audio using the recording object.
    """
    rec = recording.Recording(total_duration,delay) # recording.py object
    rec.record() # recording.py method
    





def move_audio(source_filename):
    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    date_time = now.strftime("%Y%m%d_%H_%M_%S")

    # Get the base name of the source file
    base_name = os.path.basename(source_filename)

    # Add the date and time to the base name
    new_base_name = f"{date_time}_{base_name}"

    # Create the destination filename
    destination_directory = "../audio_files/source/detection"
    destination_filename = os.path.join(destination_directory, new_base_name)

    # Move the file
    shutil.move(source_filename, destination_filename)       
    

    
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
    features = features_extraction.Extract()
    model = model_import.ModelPredictor()
    i = 0 # counter
    timestamps = []
    
    while True:
        if i == 0:
            time.sleep(delay+1) # wait 
            print("Processing started...")
            if os.path.exists(f"../audio_files/source/source{i}.wav"):
                timestamps.append(datetime.now())
                processor.adjust_volume(f"../audio_files/source/source{i}.wav")
                processor.read_audio(f"../audio_files/source/source{i}.wav", file_path_noise) # read the file
                processor.process_audio(f"../audio_files/effected/effected{i}.wav")     # process the file
                features.extraction(f"../audio_files/effected/effected{i}.wav")
                result = model.process()
                if result == 1:
                    move_audio(f"../audio_files/source/source{i}.wav")
                    print(f"Scream detected at {timestamps[i]}!")
            i = i + 1
        else:
            time.sleep(delay) # wait
            if os.path.exists(f"../audio_files/source/source{i}.wav"): # if the file exists
                timestamps.append(datetime.now())
                processor.adjust_volume(f"../audio_files/source/source{i}.wav")
                processor.read_audio(f"../audio_files/source/source{i}.wav", file_path_noise) # read the file
                processor.process_audio(f"../audio_files/effected/effected{i}.wav") # process the file
                features.extraction(f"../audio_files/effected/effected{i}.wav")
                result = model.process()
                if result == 1:
                    move_audio(f"../audio_files/source/source{i}.wav")
                    print(f"Scream detected at {timestamps[i]}!")
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

    print("Recording finished.")

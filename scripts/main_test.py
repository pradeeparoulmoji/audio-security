import noise_reduction_clean
import recording
import threading
import time


def main():
    # Creating instances 
    rec = recording.Recording() # recording.py
    #nr = noise_reduction_clean.NoiseReduction() # noise_reduction_clean.py

    

    # methods
    rec.record()
    #nr.process_audio()
    

#if __name__ == "__main__":
main()



from pydub import AudioSegment
import os


def segment_audio_file(file_path, dest_dir, chunk_duration_ms=2000):
    # Check if it's a file and has a ".wav" extension (adjust extension as needed)
    if os.path.isfile(file_path) and file_path.lower().endswith('.wav'):
        # Load the audio file
        audio = AudioSegment.from_file(file_path, format="wav")

        # Get the duration of the audio in milliseconds
        duration_ms = len(audio)

        # Calculate the number of chunks
        num_chunks = duration_ms // chunk_duration_ms

        # Segment the audio into chunks
        audio_chunks = [audio[i * chunk_duration_ms : (i + 1) * chunk_duration_ms] for i in range(num_chunks)]

        # Save each chunk
        for i, chunk in enumerate(audio_chunks):
            output_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}_chunk{i+1}.wav"
            output_path = os.path.join(dest_dir, output_filename)
            chunk.export(output_path, format="wav")
            
adjust_volume('C:/Users/tm2378/Desktop/test/effected1.wav')   

segment_audio_file('C:/Users/tm2378/Desktop/test/effected1.wav', 'C:/Users/tm2378/Desktop/test', 2000)            
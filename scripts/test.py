import noise_reduction_clean




file_path = "C:/Users/tm2378/Desktop/TIROCINIO/WAV/more2.wav"
file_path_noise = "C:/Users/tm2378/Desktop/TIROCINIO/WAV/noises.wav"
file_path_dest = 'C:/Users/tm2378/Desktop/TIROCINIO/WAV/effectedoooooooooooooo.wav'
processor = noise_reduction_clean.PreProcessing(file_path, file_path_dest)
noise_reduction_clean.processor.read_audio(file_path,file_path_noise)

noise_reduction_clean.processor.process_audio()

noise_reduction_clean.processor.plot_audio_channels() #original audio plot


noise_reduction_clean.processor.read_audio(file_path_dest,file_path_noise)

noise_reduction_clean.processor.plot_audio_channels() #processed audio plot

print("finished")

#Note finali: ad ogni finestra matplotlib che si apre, per visualizzare la successiva bidsogna chiudere la precedente


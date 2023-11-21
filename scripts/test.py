import noise_reduction_clean




file_path = "C:/Users/tm2378/Documents/GitHub/audio-security/audio_files/more2.wav"
file_path_noise = "C:/Users/tm2378/Documents/GitHub/audio-security/audio_files/noises.wav"
file_path_dest = "C:/Users/tm2378/Documents/GitHub/audio-security/audio_files/effected.wav"
processor = noise_reduction_clean.PreProcessing(file_path, file_path_dest)
processor.read_audio(file_path,file_path_noise)

processor.process_audio()

processor.plot_audio_channels() #original audio plot


processor.read_audio(file_path_dest,file_path_noise)

processor.plot_audio_channels() #processed audio plot

print("finished")

#Note finali: ad ogni finestra matplotlib che si apre, per visualizzare la successiva bidsogna chiudere la precedente


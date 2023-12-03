import noise_reduction_clean





file_path = "../audio_files/source/source.wav"
file_path_noise = "../audio_files/noises/noises.wav"
file_path_dest = "../audio_files/effected/effected.wav"
processor = noise_reduction_clean.PreProcessing()
processor.read_audio(file_path,file_path_noise)

processor.process_audio(file_path_dest)

processor.plot_audio_channels() #original audio plot


processor.read_audio(file_path_dest,file_path_noise)

processor.plot_audio_channels() #processed audio plot

print("finished")

#Note finali: ad ogni finestra matplotlib che si apre, per visualizzare la successiva bidsogna chiudere la precedente


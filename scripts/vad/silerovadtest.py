#passo l audio, a ogni chunk che dura circa 0.1 (dipende da sr e window) mi dice se ad ogni chunk c'è voce o no, risultati decenti con window 3000

#vedi onlinee scream detection e fai una media tra i due

SAMPLING_RATE = 16000 #allowed 8000 or 16000

import torch
import torchaudio
import pandas as pd
torch.set_num_threads(1) #function is a PyTorch function that sets the number of OpenMP threads used for parallelizing CPU operations.

#from IPython.display import Audio    this class can be used to create an audio control that can play audio in Jupyter notebooks.
from pprint import pprint #printing complex data structures like nested lists and dictionaries in a well-formatted and more readable way.
# download example
torch.hub.download_url_to_file('https://models.silero.ai/vad_models/en.wav', 'en_example2.wav') #arg1 = source, args2 = destination, torch hub can download files from url any kind of file on the web


USE_ONNX = False # change this to True if you want to test onnx model

    

model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                              model='silero_vad',
                              force_reload=True,
                              onnx=USE_ONNX) #The function returns two values: the loaded model, and a utility object (often a module or a dictionary) that contains helper functions or additional information about the model. 

(get_speech_timestamps,
 save_audio,
 read_audio,
 VADIterator,
 collect_chunks) = utils

'''''
wav = read_audio('en_example.wav', sampling_rate=SAMPLING_RATE)
# get speech timestamps from full audio file
speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=SAMPLING_RATE)
pprint(speech_timestamps)

# merge all speech chunks to one audio
save_audio('only_speech.wav', collect_chunks(speech_timestamps, wav), sampling_rate=SAMPLING_RATE) #save only chunks where there is voice
'''''




## just probabilities, ogni chunk dura circa 0.01 secondi
vad_iterator = VADIterator(model)
wav = read_audio('effected999999999.wav', sampling_rate=SAMPLING_RATE)
speech_probs = []
window_size_samples = 3000
for i in range(0, len(wav), window_size_samples):
    chunk = wav[i: i+ window_size_samples]
    if len(chunk) < window_size_samples:
      break
    speech_prob = model(chunk, SAMPLING_RATE).item()
    speech_probs.append(speech_prob)
vad_iterator.reset_states() # reset model states after each audio

print(speech_probs, len(speech_probs), 16000/1536*30) # first 10 chunks predicts

df = pd.DataFrame(speech_probs, columns=['Speech Probability'])

df = df.assign(time=lambda df: (df.index * window_size_samples) / SAMPLING_RATE)

df.to_excel("output.xlsx")

print(df)
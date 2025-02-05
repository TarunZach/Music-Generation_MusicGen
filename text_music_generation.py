# -*- coding: utf-8 -*-
"""Text-music_generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QRCic3w-1yZ7yIAArWCtW6nNENrQG-P-

# Overview of Meta's MusicGen
MusicGen is a remarkable model designed for music generation that offers simplicity and controllability. Unlike existing methods such as MusicLM, MusicGen stands out by eliminating the need for a self-supervised semantic representation. The model employs a single-stage auto-regressive Transformer architecture and is trained using a 32kHz EnCodec tokenizer. Notably, MusicGen generates all four codebooks in a single pass, setting it apart from conventional approaches. By introducing a slight delay between the codebooks, the model demonstrates the ability to predict them in parallel, resulting in a mere 50 auto-regressive steps per second of audio. This innovative approach optimizes the efficiency and speed of the music generation process.

MusicGen is trained on 20K hours of licensed music to train MusicGen. They also trained it on the internal dataset of 10K high-quality music tracks, and on the ShutterStock and Pond5 music data.
"""

!nvidia-smi

"""# Installation"""

# install the audiocraft liabrary from github
!python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft

"""# Import necessary libraries"""

# import necessary libraries
from audiocraft.models import musicgen
from audiocraft.utils.notebook import display_audio
import torch
from audiocraft.data.audio import audio_write
import torchaudio

"""# Loading the model"""

# | model types are =>      small,  medium,   melody,   large |
# | size of models are =>   300M,   1.5B,     1.5B,     3.3B  |

# model = musicgen.MusicGen.get_pretrained('large', device='cuda')
model = musicgen.MusicGen.get_pretrained('melody', device='cuda')

"""# Setting the parameters (optional)"""

new_generation_params = { 'use_sampling': True, 'temp': 1.0, 'top_k': 250,
                         'top_p': 0.0, 'cfg_coef': 3.0, 'two_step_cfg': False }
model.generation_params = new_generation_params
model.generation_params

"""# Setting the audio length and providing text input"""

# to set a single parameter, length of the audio
model.set_generation_params(duration=30)
prompt_text = 'Happy themed music with piano and flute'
# this will generate the audio from the text
res = model.generate( [ prompt_text ], progress=True)

# display the audio with the controls
display_audio(res, 32000)

"""# Generating Unconditional music"""

res = model.generate_unconditional( num_samples=1, progress=True)
display_audio(res, 16000)

"""# Generate Conditional music ( Based on the user input )"""

prompt_text = 'Happy themed music with piano and flute'
# this will generate the audio from the text
conditional_audio = model.generate( [ prompt_text ], progress=True)

# display the audio with the controls
display_audio(conditional_audio, 32000)

"""# Write audio file to disk"""

# write the file to the disk
# takes output and file's starting string
def write_wav(output, file_initials):
  try:
    for idx, one_wav in enumerate(output):
      audio_write(f'{file_initials}_{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
      return True
  except Exception as e:
    print("error while writing the file ", e)
    return None

# this will write a file that starts with bollywood
write_wav(conditional_audio, "jigle-bell-violin-piano-1")

"""# To generate music continuation
User input + audio file
"""

path_to_audio = "/content/jigle-bell-violin-piano-1_0.wav"
description = "add heavy drums, rock drums"

# Load audio from a file. Make sure to trim the file if it is too long!
prompt_waveform, prompt_sr = torchaudio.load( path_to_audio )
prompt_duration = 10
prompt_waveform = prompt_waveform[..., :int(prompt_duration * prompt_sr)]
output = model.generate_continuation(prompt_waveform, prompt_sample_rate=prompt_sr,
                                     descriptions=[ description ], progress=True)
write_wav(conditional_audio, "jigle-bell-violin-piano-drums")
display_audio(output, sample_rate=32000)

"""# Melody-conditional Generation"""

# model = MusicGen.get_pretrained('melody')
model = musicgen.MusicGen.get_pretrained('melody', device='cuda')

model.set_generation_params(duration=10)

melody_waveform, sr = torchaudio.load("/content/jigle-bell-violin-piano-1_0.wav")
melody_waveform = melody_waveform.unsqueeze(0).repeat(1, 1, 1)
output = model.generate_with_chroma(
    descriptions=[ 'add flute, heavy flute' ],
    melody_wavs=melody_waveform,
    melody_sample_rate=sr,
    progress=True
)
write_wav(conditional_audio, "jigle-bell-violin-piano-flute")
display_audio(output, sample_rate=32000)


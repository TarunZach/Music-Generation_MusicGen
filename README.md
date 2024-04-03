# MusicGen

## Introduction

MusicGen is an advanced model designed for music generation, leveraging state-of-the-art deep learning techniques. Unlike traditional approaches, MusicGen offers simplicity and controllability, making it a versatile tool for music composition. Powered by a single-stage auto-regressive Transformer architecture, MusicGen eliminates the need for self-supervised semantic representation, allowing for efficient and rapid music generation.

## Key Features

- Utilizes a Transformer architecture for music generation.
- Trained on a large dataset of licensed music tracks.
- Capable of generating diverse and contextually relevant music compositions.
- Offers controllability through user-defined text prompts.
- Supports conditional and unconditional music generation.

## Uses and Applications

MusicGen finds applications in various domains, including:

- Media Production: Generate background music for videos, films, and advertisements.
- Music Composition: Assist composers in generating new musical ideas and motifs.
- Education: Provide interactive tools for teaching music theory and composition.
- Entertainment: Create personalized music playlists and soundtracks.

## How to Run the Code

**Notice** : If you are planning on using CUDA through Visual Studio Code then follow these steps to create a virtual environment along with downloading the CUDA Toolkit 
  - https://amansingh3110.medium.com/how-to-set-up-cuda-environment-for-jupyter-notebooks-vscode-a-comprehensive-guide-669f00ba07f7
    
    ```python -m venv virtualenvname```
    
    Replace virtualenvname with your desired virtual environment name.

    Inside your virtual environment, install Jupyter and IPykernel using the following commands:
    
    ```pip install ipykernel jupyter```

    Now, install PyTorch with CUDA support. Make sure to check the official PyTorch website for the latest installation instructions. Typically, you can use the following command:
    
    OSX - 
    ```pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1```

    Linux and Windows -
    
    ```
    # ROCM 5.7 (Linux only)
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/rocm5.7
    # CUDA 11.8
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cpu
    ```

To run the provided code, follow these steps:

1. **Install Required Libraries:**
   Before running the code, ensure that you have installed the necessary libraries. You can install them using pip:

   ```
   pip install audiocraft torch torchaudio
   !python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft
    
   !pip install librosa mir_eval
   
   #In case of errors, try installing the right version
   !pip install audiocraft
    
   !pip install --upgrade torch
    
   !pip install --upgrade torchaudio
   ```

2. **Run the Notebook**


   
   

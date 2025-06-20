# recorder.py

import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(
    duration: int = 2,
    samplerate: int = 44100,
    channels: int = 1,
    output_path: str = "temp_audio/output.wav"
) -> str:
    """
    Records audio from the default input device and writes it to a .wav file.

    Args:
        duration (int): Duration of recording in seconds.
        samplerate (int): Audio sample rate.
        channels (int): Number of input channels.
        output_path (str): Filepath to save the audio recording.

    Returns:
        str: The path to the recorded .wav file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"🎙️ Recording {duration}s to '{output_path}'...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()
    
    write(output_path, samplerate, audio)
    return output_path

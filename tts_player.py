import os
import simpleaudio as sa

def play_audio(path: str) -> None:
    if not path.endswith(".wav"):
        raise ValueError("Only .wav files are supported.")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Audio file not found: {path}")
    print(f"(Simulated playback): {path}")
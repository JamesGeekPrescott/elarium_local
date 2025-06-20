# recorder.py
import os
import numpy as np
import wave

def record_audio(
    duration: int = 2,
    samplerate: int = 44100,
    channels: int = 1,
    output_path: str = "temp_audio/output.wav"
) -> str:
    """
    Records audio from the default input device and writes it to a .wav file.
    """
    # 👇 Lazy-import inside function to allow mocking in CI
    import sounddevice as sd

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"🎙️ Recording {duration}s to '{output_path}'...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()

    write(output_path, samplerate, audio)
    return output_path

def write(path, samplerate, audio):
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(audio.shape[1] if audio.ndim > 1 else 1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
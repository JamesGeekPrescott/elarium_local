import subprocess
import os
import tempfile

WHISPER_EXECUTABLE = os.path.abspath(
    os.path.join("..", "whisper.cpp", "build", "bin", "Release", "whisper-cli.exe")
)
MODEL_PATH = os.path.abspath(os.path.join("..", "whisper.cpp", "ggml-base.bin"))


def transcribe(audio_path):
    """
    Transcribes the given .wav file using whisper-cli.exe and returns the output as a string.
    """

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if not os.path.exists(WHISPER_EXECUTABLE):
        raise FileNotFoundError(f"Whisper CLI not found: {WHISPER_EXECUTABLE}")

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

    try:
        result = subprocess.run(
            [
                WHISPER_EXECUTABLE,
                "-m", MODEL_PATH,
                "-f", audio_path
            ],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error during transcription: {e.stderr}"

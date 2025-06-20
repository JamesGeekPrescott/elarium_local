import os
import sys
import pytest

# Ensure the recorder module is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from recorder import record_audio


def test_record_creates_audio_file():
    output_path = record_audio()
    assert os.path.exists(output_path), "Expected output .wav file to exist"
    assert output_path.endswith(".wav"), "Expected output file to be a .wav"


def test_record_file_is_in_temp_audio_folder():
    output_path = record_audio()
    assert "temp_audio" in output_path.replace("\\", "/"), "File should be saved inside 'temp_audio' folder"


def test_recorded_file_is_not_empty():
    output_path = record_audio()
    assert os.path.getsize(output_path) > 44, "Recorded file should contain audio data beyond WAV header (44B)"


def test_record_audio_accepts_custom_filename():
    custom_path = "temp_audio/custom_test.wav"
    output_path = record_audio(output_path=custom_path)
    assert output_path == custom_path, "Function should return the custom output path"
    assert os.path.exists(custom_path), "Expected custom output file to exist"


def test_record_audio_raises_on_invalid_path():
    with pytest.raises(Exception):
        record_audio(output_path="Z:/this/path/should/not/exist/audio.wav")


def test_record_audio_raises_if_input_device_invalid():
    import sounddevice as sd

    # Backup and set invalid device
    original_device = sd.default.device
    invalid_device = 99999  # unlikely to exist
    sd.default.device = (invalid_device, None)

    try:
        with pytest.raises(Exception):
            record_audio()
    finally:
        # Restore device
        sd.default.device = original_device
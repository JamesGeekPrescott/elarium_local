import sys
import os
import pytest
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transcribe_whisper import transcribe

def test_transcribe_returns_non_empty_text():
    dummy_audio_path = "temp_audio/output.wav"
    
    # Make sure the file exists for the test (you can pre-record it)
    assert os.path.exists(dummy_audio_path), "Missing audio file for transcription test"
    
    result = transcribe(dummy_audio_path)
    assert isinstance(result, str), "Transcription result should be a string"
    assert len(result.strip()) > 0, "Transcription result should not be empty"

def test_transcription_contains_timestamps():
    dummy_audio_path = "temp_audio/output.wav"
    assert os.path.exists(dummy_audio_path), "Missing audio file for transcription test"

    result = transcribe(dummy_audio_path)

    # Check for timestamp format like [00:00:00.000 --> 00:00:02.000]
    assert "[00:" in result and "-->" in result, "Expected timestamp format in transcription output"

def test_transcription_structure_matches_timestamped_pattern():
    dummy_audio_path = "temp_audio/output.wav"
    assert os.path.exists(dummy_audio_path), "Missing audio file for transcription structure test"

    result = transcribe(dummy_audio_path)

    pattern = re.compile(r"\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]\s+.+")
    matches = pattern.findall(result)

    assert matches, "No valid timestamped segments found in transcription output"

# Behavior Contract: `record_audio()`

## Module: recorder.py

## Function Signature
```python
record_audio(
    duration: int = 2,
    samplerate: int = 44100,
    channels: int = 1,
    output_path: str = "temp_audio/output.wav"
) -> str
```

## Responsibilities
- Records audio from the system's default input device (e.g., microphone).
- Saves the recording as a `.wav` file to the specified `output_path`.
- Ensures the parent directory of `output_path` exists before writing.
- Returns the file path after successful creation.

## Inputs
| Parameter     | Type  | Description                                  |
|---------------|-------|----------------------------------------------|
| duration      | int   | Length of audio to record (in seconds)       |
| samplerate    | int   | Audio sample rate (e.g. 44100 Hz)            |
| channels      | int   | Number of input channels (usually 1 or 2)    |
| output_path   | str   | Destination path for the output `.wav` file  |

## Outputs
- Returns: `str` – the full path to the recorded `.wav` file

## Guarantees
- The returned file **exists** and is a valid `.wav` file.
- The file is **not empty** (typically > 44 bytes for WAV header).
- The file is saved in the correct directory (e.g., `temp_audio/`).
- The function supports custom filenames via `output_path`.

## Error Behavior
- Raises `OSError` or similar if the path cannot be written.
- Raises `PortAudioError` or equivalent if the mic device is unavailable.
- These exceptions are not suppressed—testable at the call level.

## Tested Behaviors
- ✅ Creates a `.wav` file when called with default params
- ✅ Allows a custom output filename
- ✅ Produces a file inside `temp_audio/`
- ✅ File is not empty
- ✅ Fails if given a bad output path
- ✅ Fails if mic input device is unavailable

## Future Improvements (Cycle 2+)
- Add user-friendly error messages for exceptions
- Add duration-based file size estimation for validation
- Add fallback to synthetic or stub audio in mic-unavailable cases
## 📁 Project Structure

- `.env`
- `.gitignore`
- `.pytest_cache/` *(directory)*
- `1.0`
- `README.md`
- `config.json`
- `config.py`
- `docs/` *(directory)*
- `logs/` *(directory)*
- `main.py`
- `model_interface.py`
- `pip`
- `pytest`
- `pytest.ini`
- `recorder.py`
- `requirements.txt`
- `sounddevice)`
- `temp_audio/` *(directory)*
- `tests/` *(directory)*
- `tests_local/` *(directory)*
- `transcribe_whisper.py`
- `tts_player.py`


---

## 🧪 Testing

This project uses **Pytest** for test coverage.

### 🧼 Structure

- `tests/` – Core unit tests
- `tests_local/` – Optional tests that use system resources (e.g. microphone)

### ✅ Run All Tests
```bash
pytest tests/ tests_local/
```

### 🧪 Run Only Core Tests (CI-safe)
```bash
pytest tests/
```

> ⚠️ Note: `tests_local/` contains tests that may fail on CI environments. These are excluded by default using `pytest.ini`.

---

## 📦 Contributing Setup

### 🛠️ First-Time Setup

```bash
git clone https://github.com/jamesgeekprescott/elarium_local.git
cd elarium_local
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### 🌿 Working Safely

We recommend working on a **separate branch**:

```bash
git checkout -b dev
```

And pushing like so:

```bash
git push origin dev
```

---

## ⚖️ License

MIT License. See `LICENSE` file if available. (You may still need to add it.)

---

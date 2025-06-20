# conftest.py
import sys
import os

if os.getenv("CI"):
    from unittest import mock
    sys.modules["sounddevice"] = mock.MagicMock()

from __future__ import annotations

from cx_Freeze import Executable, setup

setup(
    name="voice-translator",
    version="0.1",
    description="Real-Time Voice Translator GUI",
    executables=[Executable("main.py")],
    options={
        "build_exe": {
            "include_files": [("icon.png")],
            "zip_include_packages": ["env/"],
            "zip_exclude_packages": [],
        }
    },
)
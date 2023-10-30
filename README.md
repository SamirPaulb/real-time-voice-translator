<div align="center">
<h1> Real-Time Voice🎙️ Translator🔊 </h1> <a href="#"><img alt="language" src="https://github.com/SamirPaulb/real-time-voice-translator/assets/132539454/5d9bd32d-48d3-474b-9108-5961179ab9af"></a>

A machine learning project that translates voice from one language to another in real-time while preserving the tone and emotion of the speaker, and outputs the result in MP3 format.
</div>

### Dependencies
    Python3, SpeechRecognition, pyaudio, google-trans-new, gTTS, playsound, deep-translator, cx-Freeze

### Getting started

1. Clone this project and create virtualenv (recommended) and activate virtualenv.
    ```
    # Create virtualenv
    virtualenv -p python3 env
 
    # Linux/MacOS
    source env/bin/activate
    
    # Windows
    env\Scripts\activate
    ```
    
2. Install require dependencies.
    ```
    pip install -r requirements.txt
    ```

3. Run code and speech (have fun).
    ```
    python main.py
    ```

### Install Desktop Application
I am using [cx_Freeze](https://github.com/marcelotduarte/cx_Freeze/tree/main) to build executable file of this app. The build settings can be changed by modifying the [setup.py](./setup.py) file.

- Build option:
    ```
    python setup.py build
    ```
- Installer containing all the files:
    ```
    python setup.py bdist_msi
    ```

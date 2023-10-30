<div align="center">
<h1> Real-Time Voice🎙️ Translator🔊 </h1> <a href="#"><img alt="language" src="https://user-images.githubusercontent.com/132539454/278971782-9453805e-e2e6-4d99-b1de-cf8fcd3e7105.svg"></a>

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

### Install Desktop Application <a href="https://github.com/SamirPaulb/real-time-voice-translator/releases/latest"><img src="https://user-images.githubusercontent.com/132539454/278971282-8d676023-a03a-463c-8e55-3f0afe6e3e58.svg" alt="DOWNLOAD"></a>

I am using <a href="https://github.com/marcelotduarte/cx_Freeze/tree/main" cx_Freeze></a> to build executable file of this app. The build settings can be changed by modifying the <a href="https://github.com/SamirPaulb/real-time-voice-translator/blob/main/setup.py" setup.py></a> file.

- Build option:
    ```
    python setup.py build
    ```
- Installer containing all the files:
    ```
    python setup.py bdist_msi
    ```

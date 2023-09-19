<div align="center">
<h1> Real-Time Voice Translator </h1> <a href="#"><img alt="language" src="https://github.com/SamirPaul1/real-time-voice-translator/assets/132539454/5d9bd32d-48d3-474b-9108-5961179ab9af"></a>

A machine learning project that translates voice from one language to another in real-time while preserving the tone and emotion of the speaker, and outputs the result in MP3 format.
</div>

### Dependencies
    Python3, SpeechRecognition, pyaudio, google-trans-new, gTTS, playsound, deep-translator

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



### Problems and Solutions
- **Google Translate API error 404**: This error occurs when the Google Translate API is not available or the request is not valid. To fix this, we will use the ```deep_translator``` library instead of ```google_trans_new```.
- **Speech recognition does not work for continuous input**: The ```speech_recognition.Recognizer().listen()``` method does not work for continuous input data. To fix this, we will use the ```record()``` method with a timer.

### TODO
Update the ```record()``` timer to listen until the speaker stops speaking.

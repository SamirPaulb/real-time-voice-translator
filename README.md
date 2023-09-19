# Real-Time Voice Translator
A machine learning project that translates voice from one language to another in real-time while preserving the tone and emotion of the speaker, and outputs the result in MP3 format.

### Problems and Solutions
- **Google Translate API error 404**: This error occurs when the Google Translate API is not available or the request is not valid. To fix this, we will use the ```deep_translator``` library instead of ```google_trans_new```.
- **Speech recognition does not work for continuous input**: The ```speech_recognition.Recognizer().listen()``` method does not work for continuous input data. To fix this, we will use the ```record()``` method with a timer.

### TODO
Update the ```record()``` timer to listen until the speaker stops speaking.
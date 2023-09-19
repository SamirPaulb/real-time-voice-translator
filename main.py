import speech_recognition as sr 
# from google_trans_new import google_translator 
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator = GoogleTranslator()

while True:
	with sr.Microphone() as source:
		print("Speak Now!")
		audio = r.record(source, duration=5)
		try:
			speech_text = r.recognize_google(audio)
			print(speech_text)
			if speech_text.lower() in {'exit', 'stop'}:
				break
		except sr.UnknownValueError:
			print("Could not understand!")
		except sr.RequestError:
			print("Could not request from google")
		
		translated_test = GoogleTranslator(source='auto', target='hi').translate(text=speech_text)
		print(translated_test)

		voice = gTTS(translated_test, lang='hi')
		voice.save('voice.mp3')
		playsound('voice.mp3')
		os.remove('voice.mp3')


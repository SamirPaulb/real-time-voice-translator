import tkinter as tk
import threading
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

keep_running = False

def update_translation():
    global keep_running

    if keep_running:
        r = sr.Recognizer()
        translator = GoogleTranslator()

        with sr.Microphone() as source:
            log_output.insert(tk.END, "Speak Now!\n")
            audio = r.listen(source)
            
            try:
                speech_text = r.recognize_google(audio)
                print(speech_text)
                if speech_text.lower() in {'exit', 'stop'}:
                    keep_running = False
                    return
                
                translated_text = GoogleTranslator(source='auto', target='hi').translate(text=speech_text)
                print(translated_text)

                voice = gTTS(translated_text, lang='hi')
                voice.save('voice.mp3')
                playsound('voice.mp3')
                os.remove('voice.mp3')

                log_output.insert(tk.END, translated_text + "\n")
                
            except sr.UnknownValueError:
                log_output.insert(tk.END, "Could not understand!\n")
            except sr.RequestError:
                log_output.insert(tk.END, "Could not request from Google!\n")

    root.after(100, update_translation)

def run_translator():
    global keep_running
    
    if not keep_running:
        keep_running = True
        update_translation_thread = threading.Thread(target=update_translation)
        update_translation_thread.start()

def kill_execution():
    global keep_running
    keep_running = False

# Create the main window
root = tk.Tk()
root.title("Voice Translator GUI")

# Create the frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create the "Run" button
run_button = tk.Button(button_frame, text="Start Translation", command=run_translator)
run_button.pack(side=tk.LEFT, padx=10)

# Create the "Kill" button
kill_button = tk.Button(button_frame, text="Kill Execution", command=kill_execution)
kill_button.pack(side=tk.LEFT, padx=10)

# Create the log output window
log_output = tk.Text(root, height=20, width=50)
log_output.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

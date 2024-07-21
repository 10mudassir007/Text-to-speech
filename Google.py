import os
from gtts import gTTS

text = input('Enter to text to play : \n            ')

tts = gTTS(text = text, lang= 'en')

tts.save('text_to_speech.mp3')

os.system('start text_to_speech.mp3')
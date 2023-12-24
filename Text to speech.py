import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
select_rate = int(input('Enter speed of speech(in terms of words per minute,150 is the normal) : '))
select_volume = int(input('Enter volume 0 to 100 : '))/100
# Set properties (optional)
engine.setProperty('rate', select_rate)  # Speed of speech
engine.setProperty('volume', select_volume)  # Volume level (0.0 to 1.0)
voices = engine.getProperty('voices')
select_voice = int(input('Enter 0 for male voice and 1 for female voice : '))
if select_voice == 0:
    engine.setProperty('voice', voices[0].id)
if select_voice == 1:
    engine.setProperty('voice', voices[1].id)
# Convert text to speech
text = input('Enter text to speak : ')
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()


save_file = input('Save file, Y/N : ')
if save_file == 'Y':
    name = input('Enter name of file with extension : ')
    engine.save_to_file(text,name)                




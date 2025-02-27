from gtts import gTTS
from playsound import playsound
import tempfile
import os

text = input("Enter your text: ")
language = input("Enter language code (en for english, tl for tagalog): ")

if language not in ['en', 'tl']:
    print("Invalid language. Defaulting to english.")
    language = 'en'

output = gTTS(text=text, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")
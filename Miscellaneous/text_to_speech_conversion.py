from gtts import gTTS
import os

mytxt = 'I am a student.'

language = 'en'

myobj = gTTS(text=mytxt, lang=language, slow=False)

myobj.save("Testfile.mp3")

os.system("mpg321 Testfile.mp3")

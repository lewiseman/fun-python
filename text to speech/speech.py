from gtts import gTTS 
import os

# f = open('good.txt')
# x = f.read()
text = "you have no work"

language = 'en'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("good.mp3")

os.system("good.mp3")
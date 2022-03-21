from gtts import gTTS
import os

file = open("Favoritenovel.txt", "r").read().replace("\n", "")


languaje = "es-us"

speech = gTTS (text = str(file), lang = languaje, slow = False)

speech.save("audio.mp4")

os.system("start audio.mp4")


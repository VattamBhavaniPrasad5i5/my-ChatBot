# import subprocess
# from gtts import gTTS

# mytext = "this is prasad 1"
# language = 'en'
# # Convert the text to speech
# tts = gTTS(text=mytext, lang=language)

# # Save the speech to a file
# tts.save("hello.mp3")
# # Playing the converting file
# subprocess.run(['mpyg321', "hello.mp3", '-q'])
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

from playsound import playsound

# It is a text value that we want to convert to audio
text_val = 'hellow gmrit'

# Here are converting in English Language
language = 'en'

# Passing the text and language to the engine,
# here we have assign slow=False. Which denotes
# the module that the transformed audio should
# have a high speed
obj = gTTS(text=text_val, lang=language, slow=False)

# Here we are saving the transformed audio in a mp3 file named
# exam.mp3
obj.save("exam.mp3")

# Play the exam.mp3 file
playsound("exam.mp3")

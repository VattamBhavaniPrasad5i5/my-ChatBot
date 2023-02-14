import requests
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr

#sender = input("What is your name")
bot_message = ""
while bot_message != "Bye" or bot_message != 'thanks':
    r = sr.Recognizer()
    message = ""

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Speak Anything...")
        audio_text = r.listen(source)

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            message = r.recognize_google(audio_text)
            print("You Said : {}".format(message))
        except:
            print("Sorry, I did not get that")

    if len(message) == 0:
        #message = ""
        continue
    print("Sending message now...")

    r = requests.post(
        'http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("jarvis says,")
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
    language = 'en'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=bot_message, lang=language)

    # Here we are saving the transformed audio in a mp3 file named
    # exam.mp3
    obj.save("exam.mp3")

    # Play the exam.mp3 file
    playsound("exam.mp3")

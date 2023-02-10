import requests

sender = input("What is your name")
bot_message = ""
while bot_message != "Bye":
    message = input("What is your message?\n")

    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook',
                      json={"sender": sender, "message": message})

    print("Bot says,", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")

from notifypy import Notify
import winsound
import requests
import time
import functools
import webbrowser

notification = Notify()

def get(url):
    r = requests.get(url)
    return r.json()

def sendNotification(playingUrl):
    notification.title = "Lichess"
    notification.message = "FM Jaboder ist online und spielt hier: " + playingUrl
    notification.icon = "lichess.png"
    notification.send()
    winsound.PlaySound("notification-sound.wav", winsound.SND_FILENAME)
    

isNotOnline = True

#Jaboder

while isNotOnline:
    [response] = get("https://lichess.org/api/users/status?ids=Jaboder")
    if {"online"} <= response.keys():
        response = get("https://lichess.org/api/user/Jaboder")
        if {"playing"} <= response.keys():
            playingUrl = response["playing"]
            sendNotification(playingUrl)
            webbrowser.open(playingUrl)
            isNotOnline = False
    time.sleep(5)

print("End Programm")


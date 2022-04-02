from threading import Thread
import requests

mytuple = {
    'facebook': 'False',
    'tumblr': 'False',
    'instagram': 'False',
    'twitter': 'False',
    'steam': 'False',
    'snapchat': 'False',
    'twitch': 'False',
    'tiktok': 'False',
}

def getRequest(username, link):
    headers = {"Content-Type": "application/json; charset=utf-8"}

    return requests.get(link+username, headers=headers)

def facebook(username):
    link = "https://www.facebook.com/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userFacebook = link + username
        mytuple['facebook'] = userFacebook

def tumblr(username):
    link = "http://www.tumblr.com/blog/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userTumblr = link + username
        mytuple['tumblr'] = userTumblr

def instagram(username):
    link = "https://www.instagram.com/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userInstagram = link + username
        mytuple['instagram'] = userInstagram

def twitter(username):
    link = "http://www.twitter.com/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userTwitter = link + username
        mytuple['twitter'] = userTwitter
       
def steam(username):
    link = "https://steamcommunity.com/id/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userSteam = link + username
        mytuple['steam'] = userSteam

def snapchat(username):
    link = "https://www.snapchat.com/add/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userSnapchat = link + username
        mytuple['snapchat'] = userSnapchat

def twitch(username):
    link = "https://www.twitch.tv/"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userTwitch = link + username
        mytuple['twitch'] = userTwitch

def tiktok(username):
    link = "https://www.tiktok.com/@"
    answer = getRequest(username, link)
    if answer.status_code == 200:
        userTiktok = link + username
        mytuple['tiktok'] = userTiktok

def getData(username):

    Thread(target=facebook, args=(username,)).start()
    Thread(target=tumblr, args=(username,)).start()
    Thread(target=instagram, args=(username,)).start()
    Thread(target=twitter, args=(username,)).start()
    Thread(target=steam, args=(username,)).start()
    Thread(target=snapchat, args=(username,)).start()
    Thread(target=twitch(username), args=(username,)).start()
    Thread(target=tiktok(username), args=(username,)).start()
    return mytuple
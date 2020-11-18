import config

import urllib
import urllib2
import platform
import os

system = str(platform.system())+" - "+str(os.name) + " ver " + str(platform.release())


def send(id, text):
    resp = urllib2.urlopen(config.BASE_URL + 'sendMessage', urllib.urlencode({
        'chat_id' : id,
        'text': text.encode('utf-8'),
        })).read()
    return resp

def base(update):
    #send(update['message']['from']['id'], str(update))
    #send(update['message']['from']['id'], "Hello " + update['message']['from']['first_name'] + "\nUp and running on "+system+" !")
    send(update['message']['from']['id'], "Version 5")
    return 'ok'

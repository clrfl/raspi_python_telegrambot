import config
import bot
import imp

from flask import Flask, request
import urllib
import urllib2

context = (config.PUBLIC_KEYFILE, config.PRIVATE_KEYFILE)
app = Flask(__name__)


def debug(text):
    try:
        resp = urllib2.urlopen(config.BASE_URL + 'sendMessage', urllib.urlencode({
            'chat_id': config.MY_ID,
            'text': text.encode('utf-8'),
        })).read()
        return resp
    finally:
        return 'done'


@app.route(config.PATH, methods=['GET'])
def index():
    return 'dis bitch empty'


@app.route(config.PATH, methods=['POST'])
def respond():
    try:
        update = request.get_json()
        if (str(update['message']['from']['id']) == config.MY_ID and update['message']['text'] == '/reload'):

            filedata = urllib2.urlopen(config.SOURCE_URL)
            datatowrite = filedata.read()
            with open('/restricted/directory/bot.py', 'wb') as f:
                f.write(datatowrite)

            imp.reload(bot)
            debug("reloaded")
        else:
            bot.base(update)
    except Exception as e:
        debug(str(e))
    finally:
        return 'done'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=context)

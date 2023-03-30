# coding=utf-8
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf8')
import json

from google.appengine.ext import ndb
from google.appengine.api import urlfetch

class ChatgptToken(ndb.Model):
    ChatgptToken = ndb.StringProperty(indexed=False, default='')
    
def setChatgptToken(chat_id, token):
    es = ChatgptToken.get_or_insert(str(chat_id))
    es.ChatgptToken = str(token)
    es.put()

def getChatgptToken(chat_id):
    es = ChatgptToken.get_or_insert(str(chat_id))
    if es:
        return str(es.ChatgptToken)
    return ''
    
def run(bot, chat_id, user, keyConfig, message, totalResults=1):
    requestText = str(message).replace(bot.name, "").strip()
    getToken = getChatgptToken(chat_id)
    if (getToken == ""):
        bot.sendMessage(chat_id=chat_id, text='I\'m sorry ' + (user if not user == '' else 'Dave') +
                        ', no chatgpt key set. Try sending a valid Chatgpt key with /setask.')
    else:
        fetch_url = 'https://api.openai.com/v1/chat/completions '
        raw_data = urlfetch.fetch(url=fetch_url,
                                  headers={'Authorization': 'Bearer ' + getToken, 'Content-Type': 'application/json'},
                                  payload={'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': requestText}], 'temperature': 0.7}).content
        try:
            data = json.loads(raw_data)
            if ('error' in data):
                bot.sendMessage(chat_id=chat_id, text='I\'m sorry ' + (user if not user == '' else 'Dave') +
                                ',\n' + data['error']['message'])
            else:
                if ('messages' in data and len(data['messages']) > 0):
                    bot.sendMessage(chat_id=chat_id, text='\"' + data['messages'][0]['content'])
                    return True
                else:
                    bot.sendMessage(chat_id=chat_id, text='I\'m sorry ' + (user if not user == '' else 'Dave') +
                                    ', I\'m afraid I can\'t find any Chatgpt answers for ' +
                                    requestText)
        except ValueError:
            if (raw_data != ""):
                bot.sendMessage(chat_id=chat_id, text=raw_data)
            else:
                bot.sendMessage(chat_id=chat_id, text='Chatgpt api url returned nothing: ' + fetch_url)
    return False

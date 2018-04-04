import json
import logging
from channels import Channel
from channels.sessions import channel_session

from Musculando.celery import app

import json


from django.conf import settings
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.generic.websockets import WebsocketDemultiplexer


log = logging.getLogger(__name__)

@channel_session_user_from_http
def ws_connect(message):
    Group('notifcaciones').add(message.reply_channel)
    # Send a list of active users to the user.
    message.reply_channel.send({
        'text': json.dumps ({"action": "completed","content": "Conect"})
    })

@channel_session
def ws_receive(message):
  try:
     data = json.loads(message['text'])
  except ValueError:
     log.debug("ws message isn’t json text=%s", message['text'])
     return
  if data:
     reply_channel = message.reply_channel.name
     if data['action'] == 'long_process':
       Channel(reply_channel).send({"text": json.dumps ({"action": "completed","content": "long_process"})})
     else:
       Channel(reply_channel).send({'text': json.dumps ({'action': 'completed','content': 'short_process'})})



def debug(message):
  print('HOLAAAAAAAAAAAAAAAAAAAAAAAAA AQUI ESTOY')
  #reply_channel = message.reply_channel.name
  Channel('debug').send({'text': json.dumps ({'action': 'completed','content': 'short_process'})})
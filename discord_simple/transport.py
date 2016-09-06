import logging
import urllib3
import websocket
import json
import time
import certifi
import threading
from random import randint as random_integer
from .models.user import User
from .models.message import Message

class Transport:

  DISPATCH           = 0
  HEARTBEAT          = 1
  IDENTIFY           = 2
  PRESENCE           = 3
  VOICE_STATE        = 4
  VOICE_PING         = 5
  RESUME             = 6
  RECONNECT          = 7
  REQUEST_MEMBERS    = 8
  INVALIDATE_SESSION = 9
  HELLO              = 10
  HEARTBEAT_ACK      = 11
  GUILD_SYNC         = 12

  def __init__(self,token,on_connect=None,on_message=None):
    self.token=token
    self.ws=None
    self.sequence=None
    self.h=None
    self.channels={}
    self.con_connect=on_connect
    self.con_message=on_message
    self.session=None
    self.logger = logging.getLogger(__name__)
    self._api_base = 'https://discordapp.com/api/v6/{}'
    self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    self.connect()

  def get(self, endpoint):
    r=self.http.request('GET',self._api_base.format(endpoint),headers={'Authorization': 'Bot '+self.token})
    if r.status==200:
      return(json.loads(r.data.decode('utf-8')))
    else:
      return({})

  def post(self, endpoint,message):
    r=self.http.request('POST',self._api_base.format(endpoint),headers={'Content-Type': 'application/json', 'Authorization': 'Bot '+self.token},body=message.encode('utf-8'))

  def connect(self):
    r=self.get('gateway')
    self.ws = websocket.WebSocketApp(r["url"]+"/?encoding=json&v=6",
      on_message = self.on_message,
      on_error = self.on_error,
      on_close = self.on_close)
    self.ws.on_open=self.on_connect

  def run_forever(self):
    self.ws.run_forever()

  def on_close(self,ws):
    self.logger.debug("close")

  def on_message(self,ws,message):
    m=json.loads(message)
    self.sequence=m["s"]
    if m["op"] == self.DISPATCH:
      if m["t"] == "READY":
        for channel in m["d"]["private_channels"]:
          if len(channel["recipients"])==1:
            self.channels[channel["id"]]=User(channel["recipients"][0])
            self.logger.info("added channel for {}".format(self.channels[channel["id"]]))
        self.session = m["d"]["session_id"]
        self.con_connect(User(m["d"]["user"]))
      elif m["t"] == "GUILD_CREATE":
        pass
      elif m["t"] == "MESSAGE_CREATE":
        self.con_message(Message(m["d"]))
    elif m["op"] == self.HELLO:
      interval = int(m['d']['heartbeat_interval'] / 1000)
      self.h=Heartbeat(self,interval)
##      thread.start_new_thread(self.h.run,())
      threading.Thread(target=self.h.run).start()
    elif m["op"] == self.HEARTBEAT_ACK:
      pass
    else:
      self.debug(m)

  def on_error(self,ws,error):
    self.logger.debug("error")

  def on_connect(self,ws):
    msg={
      'op': self.IDENTIFY,
      'd': {
        'token': self.token,
        'properties': {
          '$os': 'lnx',
          '$browser': 'discord_simple',
          '$device': 'discord_simple',
          '$refferer': '',
          '$reffering_domain': ''
        },
        'compress': False,
        'large_threshold': 250,
        'v' : 3
      }
    }
    ws.send(json.dumps(msg))

  def send_message(self, user, message):
    self.logger.info("sending message to {}: {}".format(user, message))
    for cid in self.channels:
      if (str(self.channels[cid]) == user):
        self.logger.info(cid)
        self.post('channels/'+cid+'/messages', json.dumps({'content': message,'nonce': random_integer(-2**63, 2**63 - 1)}))

class Heartbeat:

  def __init__(self,t,interval):
    self.logger = logging.getLogger(__name__)
    self.t=t
    self.interval=interval

  def run(self):
    self.logger.info("heartbeat started")
    while True:
      time.sleep(self.interval)
      self.send_heartbeat()

  def send_heartbeat(self):
    self.logger.info("heartbeat "+str(self.t.sequence))
    self.t.ws.send(
      json.dumps(
        {
          'op': self.t.HEARTBEAT,
          'd': self.t.sequence
        }
      )
    )

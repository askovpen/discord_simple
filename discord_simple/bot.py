import logging
import json
import sys
import time
import types
from .transport import Transport

class Bot:

  def __init__(self,token,on_connect=None,on_message=None):
    self.t=None
    self.user=None
    self.token = token
    self.con_connect=on_connect
    self.con_message=on_message
    self.logger = logging.getLogger(__name__)
    self.connect()

  def connect(self):
    self.t=Transport(
      self.token,
      on_connect=self.on_connect,
      on_message=self.on_message
    )

  def on_connect(self, user):
    self.user=user
    self.logger.info("connected as {}".format(user))
    if type(self.con_connect)!=types.NoneType:
      self.con_connect(user)

  def on_message(self,data):
    if self.user.id!=data.author.id:
      self.logger.info("Message from {}: {}".format(data.author, data.content))
      if type(self.con_message)!=types.NoneType:
        self.con_message(data)

  def forever_loop(self):
    try:
      self.t.run_forever()
    except KeyboardInterrupt:
      print("inter")
      sys.exit()


  def send_message(self, user, message):
    self.t.send_message(user,message)

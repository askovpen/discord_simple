""" Todo """
import logging
import sys
from .transport import Transport

class Bot:

  """ Todo """
  def __init__(self, token, on_connect=None, on_message=None):
    self.transport = None
    self.user = None
    self.token = token
    self.con_connect = on_connect
    self.con_message = on_message
    self.logger = logging.getLogger(__name__)
    self.connect()

  def connect(self):
    """ Todo connect """
    self.transport = Transport(self.token, on_connect=self.on_connect, on_message=self.on_message)

  def on_connect(self, user):
    """ Todo connect """
    self.user = user
    self.logger.info("connected as %s", user)
    if not isinstance(self.con_connect, type(None)):
      self.con_connect(user)

  def on_message(self, data):
    """ Todo connect """
    if self.user.id != data.author.id:
      self.logger.info("Message from %s: %s", data.author, data.content)
      if not isinstance(self.con_message, type(None)):
        self.logger.debug(type(self.con_message))
        self.con_message(data)

  def forever_loop(self):
    """ Todo connect """
    try:
      self.transport.run_forever()
    except KeyboardInterrupt:
      print("inter")
      sys.exit()


  def send_message(self, user, message):
    """ Todo connect """
    self.transport.send_message(user, message)

""" Todo """
from .user import User

class Message:
  """ Todo """
  author = None
  content = None
  timestamp = None

  def __init__(self, data):
    """ Todo """
    self.author = User(data.get("author", {}))
    self.content = data.get("content", "")
    self.timestamp = data.get("timestamp", 0)

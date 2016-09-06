from .user import User
class Message:

  author=None
  content=None
  timestamp=None

  def __init__(self,data):
    self.author=User(data.get("author",{}))
    self.content=data.get("content","")
    self.timestamp=data.get("timestamp",0)

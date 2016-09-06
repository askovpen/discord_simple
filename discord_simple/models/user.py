
class User:
  id=None
  discriminator=None
  avatar=None
  verified=None
  bot=None
  username=None

  def __init__(self, data):
    self.id=data.get('id',0)
    self.username=data.get('username','')
    self.avatar=data.get('avatar',None)
    self.discriminator=int(data.get('discriminator',0))
  def __repr__(self):
    return "<User %s#%04i>" % (self.username,self.discriminator)

  def __str__(self):
    return "%s#%04i" % (self.username,self.discriminator)

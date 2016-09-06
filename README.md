# discord_simple
[![Version](https://img.shields.io/pypi/v/discord_simple.svg?maxAge=2592000)](https://pypi.python.org/pypi/discord_simple) [![Version](https://img.shields.io/pypi/pyversions/discord_simple.svg?maxAge=2592000)](https://pypi.python.org/pypi/discord_simple) 

## Installing

```
pip install -U discord.py
```

## Usage

```py
import discord_simple

bot=None

def on_connect(user):
  print("connected as "+user)
def on_message(message):
  print("message from {}: {}".format(message.author,message.content))

bot = discord_simple.Bot("your token",on_connect=on_connect,on_message=on_message)
bot.forever_loop()
```

## API

### User
* `id`
* `avatar`
* `username`
* `discriminator`

### Message
* `author`
* `content`
* `timestamp`

### Methods:
* `send_message('username#discriminator','message')`

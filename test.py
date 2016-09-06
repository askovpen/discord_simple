import discord_simple
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(threadName)s] [%(name)10s] [%(levelname)s] %(message)s'
)
logger = logging.getLogger("cli")
logger.setLevel(logging.DEBUG)

token = "insert your token"

bot=None

def on_connect(user):
  print(user)
  bot.send_message('user#12345','test')

def on_message(msg):
  print(msg.content)

bot = discord_simple.Bot(token,on_connect=on_connect,on_message=on_message)
bot.forever_loop()

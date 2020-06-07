import asyncio, osu_irc

from conf import config
from handler.pmHandler import pmHandle

class MyBot(osu_irc.Client):

  async def onReady(self):
      print('Connected!')

  async def onMessage(self, message):
      if message.channel_type == 'pm':
          await pmHandle(self, message.content, message.user_name)



x = MyBot()
x.run(nickname=config.ircName, token=config.ircPass)
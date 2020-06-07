import asyncio, osu_irc

from conf import config
from handler.pmHandler import pmHandle
from handler.channelHandler import chHandle

class MyBot(osu_irc.Client):

    async def onReady(self):
        print('Connected!')
        #await self.joinChannel('#osu')

    async def onMessage(self, message):
        if message.channel_type == 'pm':
            await pmHandle(self, message.content, message.user_name)
        if message.channel_type == 'channel':
            await chHandle(self, message.content, message.user_name, message.channel_name)

        



x = MyBot()
x.run(nickname=config.ircName, token=config.ircPass)
import discord as dc

TOKEN = 'Token in here pls'

description = '''A bot which's existence has a purpouse and one purpose only, tell you when harstem playes, and where to see it.'''
intents = dc.Intents.default() #things the bot can do/ events that can be listend to


#bot = dc.commands.Bot(command_prefix='?', description=description, intents=intents)
#@bot.command()
#async def next(channel):
#    pass

class HarstemBot(dc.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('?next'):
            await message.reply('Hello!', mention_author=True)

client = HarstemBot()
client.run(TOKEN)
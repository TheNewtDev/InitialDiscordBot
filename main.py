import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        if message.author.name == 'Vii' or message.author.name == 'vii':
            print(f"Vii said something")
            await message.channel.send(f'You\'re gay!')
        if message.author.name == "_newtnewt":
            print(f"Newt said something")
            await message.channel.send(f'You\'re the best dad ever!')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

client.run('token')


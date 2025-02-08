import discord
from discord.ext import commands
import random
import time 

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
        # if message.author.name == "_newtnewt":
        #     print(f"Newt said something")
        #     await message.channel.send(f'You\'re the best dad ever!')
        

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def annoy(ctx, *, arg):
    # mention = await get_user(arg)
    int = random.randint(1, 50)
    for i in range(int):
        await ctx.send(f'Hey Listen! {arg}')
    
@bot.command()
async def gay(ctx, * , arg):
    await ctx.send(f'Analyzing {arg}...')
    time.sleep(3)
    await ctx.send(f'{arg} is gay!')
    
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
# async def get_user(arg):
#     user = await bot.get_user(arg)
#     return user


client = Client(intents=intents)

# client.run('')
bot.run('token')


import discord
import json
from discord import ButtonStyle, ActionRow, Button
from discord.ext import commands
from discord import Color 

with open('config.json') as f:
   data = json.load(f)


TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
PREFIX = "."
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

def CreateEmbed(question, answer):
    mbd = discord.Embed(title=str(question) + ', Asking Bard')
    mbd.add_field(name = 'Answer', value = answer)
    return mbd


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(PREFIX)):
        return
    args = message.content.split(" ")
    args[0] = args[0][1::]
    print(args)
    if len(args) < 2:
        await message.channel.send('Uncorrect Format!') 
    elif args[0] == "ask-bard" :
        from askbard import AskBard
        question=   ' '.join(args[1:])
        print(question)
        answer=AskBard(question=question)
        mbd=CreateEmbed(question=question, answer=answer)
        await message.channel.send(embed=mbd) 

client.run(TOKEN)
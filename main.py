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


def CorrectAnswer(mbd, answer):
    maxlenanswer=1000
    mbd.add_field(name = 'Answer Len', value = len(answer))
    if len(answer) < maxlenanswer:
        mbd.add_field(name = 'Answer', value = answer)
    else:
        if len(answer) < 2000 :
            answer1=answer[:maxlenanswer] + '...'
            answer2=answer[maxlenanswer:]
            mbd.add_field(name = 'Part1', value = answer1)
            mbd.add_field(name = 'Part2', value = answer2)
        else:
            mbd.add_field(name = 'Error', value = 'The answer is too long.. :(')

def CorrectQuestion(question):
    maxlenquestion=120
    if len(question) > maxlenquestion:
        question=question[:maxlenquestion] + '...'
    return question

def CreateEmbed(question, answer):
    question=CorrectQuestion(question=question)
    mbd = discord.Embed(title=str(question) + ', Asking Bard')
    CorrectAnswer(mbd=mbd, answer=answer)
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
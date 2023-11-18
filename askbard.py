from bardapi import Bard
from playsound import playsound
import os
import json
with open('config.json') as f:
   data = json.load(f)
token = data['GOOGLE_TOKEN']
def AskBard(question):
    bard = Bard(token=token)
    # textinput = input("Ask Bard: ")
    answer=bard.get_answer(question+ ' make it short answer')['content']
    # audio = bard.speech(answer)
    print(answer)
    # with open("speech.ogg", "wb") as f: 
    #   f.write(bytes(audio['audio']))
    # playsound("speech.ogg")
    # os.remove("speech.ogg")
    return answer
from bardapi import Bard
from playsound import playsound
import os

token = 'dQh0WrAryeo0cmbKzwdzYejNTahjZe-XpnXBwGORVZnvoeL_H-q23xetlgptf77FTAcPyQ.'
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
from gtts import gTTS
from playsound import playsound
from playvoice import playVoice

def initGameVoice(text, player, lang, audio):
    sp = gTTS(
        text    =   text[11],
        lang    =   lang
    )
    sp.save(audio)
    playsound(audio)

    sp.text = text[1]
    sp.save(audio)
    playsound(audio)

    sp.text = text[2]
    sp.save(audio)
    playsound(audio)

    sp.text = text[12]
    sp.save(audio)
    playsound(audio)

    choice = int(input("R: "))
    

    if(choice == 1):
        rules(player, text, audio, lang)

    else:
        sp.text = text[9]
        sp.save(audio)
        playsound(audio)

        playVoice()
            


def rules(player, text, audio, lang):
    sp = gTTS(
        text    =   text[3],
        lang    =   lang
    )

    sp.save(audio)
    playsound(audio)

    sp.text = text[4]
    sp.save(audio)
    playsound(audio)

    sp.text = text[5]
    sp.save(audio)
    playsound(audio)

    sp.text = text[6]
    sp.save(audio)
    playsound(audio)

    sp.text = text[7]
    sp.save(audio)
    playsound(audio)

    sp.text = text[8]
    sp.save(audio)
    playsound(audio)

    sp.text = "Entendeu todas as regras? 1 para sim, 2 para não"
    sp.save(audio)
    playsound(audio)

    choice = int(input("R: "))
    
    if(choice == 1):
        sp.text = text[9]
        sp.save(audio)
        playsound(audio)

        playVoice()

    else:
        sp.text = text[10]
        sp.save(audio)
        playsound(audio)

        return rules(player, text, audio, lang)
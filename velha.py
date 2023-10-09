import os
import time
from gtts import gTTS
from playsound import playsound
from velhaVoice import initGameVoice

os.system('clear') or None

audio = "audio.mp3"
language = "pt-br"

sp = gTTS(
    text="Qual seu nome?",
    lang=language
)

sp.save(audio)
playsound(audio)

print("####### Configurações ############")
player = input("***Insira seu nome*** \n")

sp.text = "Prefere jogar só com texto ou só com audio? \n 1 para com texto, 2 para com audio"
sp.save(audio)
playsound(audio)

choice = input("Prefere jogar só com texto ou só com audio? \n (1) Com texto. \n (2) Com audio. \n R: ")

text = [f"|*-*|=== Bem-Vindo ===|*-*| \n",
          f"Bom {player} me chamo Velha, serei sua oponente em meu jogo.\n ",
          "O nome do meu jogo vai ser... \n \n Jogo-da-velha\n \n O que acha? \n Nem precisa responder, claro que adorou, todos adoram os nomes dos meus jogos. \n \n", 
          "Ok... \n \n",
          "As regras são as seguintes: \n \n", 
          "Regra nª1: \n Para decidir quem começa, sortearei um número entre 0 e 10.\n",
          f"Você deverá informar um número, se o seu número for maior que o meu, poderá iniciar,\n caso contrário eu iniciarei; \n \n",
          "Regra nª2: \n Para escolher onde fazer a jogada, insira as coordenadas da posição que almeja e pressione ENTER. \n Ex: \n X na linha: 2 (enter) \n X na coluna: 1 (enter) \n \n",
          "Regra nª3: \n Vence aquele que fizer uma sequência de 3 posições na horizontal / vertical ou diagonal.\n \n",
          "Que vença o melhor ;).\n \n",
          "Por que será que não estou surpresa? Essa geração nova hein...\n \n",
          "Bem-Vindo",
          "Quer saber as regras do jogo? \n 1 para sim, 2 para não."]


def initGame():
    os.system('clear') or None

    for letter in text[0]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    for letter in text[1]:
        print(letter, end='', flush=True)
        time.sleep(0.1)
    
    for letter in text[2]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    time.sleep(1)

    os.system('clear') or None

    
    choice = int(input("Quer saber as regras do jogo? \n (1)Sim \n (2)Não \n R: "))

    os.system('clear') or None

    if(choice):
        if(choice == 1):
            for letter in text[3]:
                print(letter, end='', flush=True)
                time.sleep(0.1)

            rules(player)
        else:
            for letter in text[9]:
                print(letter, end='', flush=True)
                time.sleep(0.1)
            
            import play
            play.play(player, False, False)


def rules(player):
    for letter in text[4]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    for letter in text[5]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    for letter in text[6]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    next = input("Pressione ENTER para continuar >>>")

    os.system("clear") or None

    print(text[4])

    for letter in text[7]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    next = input("Pressione ENTER para continuar >>>")

    os.system('clear') or None

    print(text[4])

    for letter in text[8]:
        print(letter, end='', flush=True)
        time.sleep(0.1)

    next = int(input(f"Entendeu {player}? \n (1)Sim. Bora jogar Velhota ;) \n (2)Não. Explique novamente por favor, o jogo é complexo demais \n para um mero mortal como eu. \n R: "))

    if(next == 1):
        for letter in text[9]:
            print(letter, end='', flush=True)
            time.sleep(0.1)

        time.sleep(1)
        os.system('clear') or None            

        import play
        return play.play(player, False, False)
    else:
        for letter in text[10]:
            print(letter, end='', flush=True)
            time.sleep(0.1)
        
        time.sleep(1)
        os.system('clear') or None            

        return rules(player)

if(choice == 1):
    initGame()
else:
    initGameVoice(text, player, language, audio)
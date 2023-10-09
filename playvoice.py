import random, os, time
from gtts import gTTS
from playsound import playsound
from pymongo import MongoClient

text = ["Informe um número de 0 a 10. \n",
        "Parabéns, pode começar! \n",
        "HAHAHAHAHAHA troxa, eu começo! \n",
        "Empatamos, vamos denovo! \n \n",
        "Opa, querendo quebrar as regras? \n Sua penalidade é perder a vez de começar. \n \n",
        "Opa, já está marcado, tente outro lugar meu jovem. \n",
        "Nããão eu fui derrotada, como?\n ... \n Você é algum tipo de Deus? \n De qualquer forma, foi um bom jogo, até nunca mais! \n",
        "AJOELHEM-SE DIANTE DE SUA DEUSA MÁQUINA \n"]

plane_game = [[0, 1, 2, 3],
              [1, " ", " ", " "],
              [2, " ", " ", " "],
              [3, " ", " ", " "]]

def playVoice(player, start, next, rp):

    if(winner(player, plane_game) == "have_win"):
        return 0
    

    for y in range(4):
        cont = 0

        for p in plane_game[y]:
            if(cont < 3):
                cont += 1
                print("", p,"|", end='')

            else: print("", p, end='')
        
        print()
        if(y<3):
            print("-----------------")

    if not start:
        start = started(player, rp)

        if(start == player):
            rp.text = "X na linha"
            rp.save(audio)
            playsound(audio)
            position_playerX = int(input("X na linha: "))

            rp.text = "X na coluna"
            rp.save(audio)
            playsound(audio)
            position_playerY = int(input("X na coluna: "))

            if(plane_game[position_playerX][position_playerY] == " "):
                plane_game[position_playerX][position_playerY] = "X"
                next = "Velha"
                os.system('clear') or None
                return playVoice(player, True, next, rp)
            
            else:
                os.system('clear') or None
                print("Valor inválido! \n \n")
                
                rp.text = text[4]
                rp.save(audio)
                playsound(audio)
                time.sleep(0.5)
                start = "Velha"
                os.system('clear') or None    
        
        if (start == "Velha"):
            position_velhaX = random.randint(1, 3)
            position_velhaY = random.randint(1, 3)
            
            if(plane_game[position_velhaX][position_velhaY] == " "):
                plane_game[position_velhaX][position_velhaY] = "O"
                rp.text = f"Circulo na linha {position_velhaX}  na coluna {position_velhaY}"
                rp.save(audio)
                playsound(audio)
                next = player

            os.system('clear') or None        
            return playVoice(player, True, next, rp)
    
    if (next == player):
        rp.text = "X na linha"
        rp.save(audio)
        playsound(audio)
        position_playerX = int(input("X na linha: "))

        rp.text = "X na coluna"
        rp.save(audio)
        playsound(audio)
        position_playerY = int(input("X na coluna: "))

        if(plane_game[position_playerX][position_playerY] == " "):
            plane_game[position_playerX][position_playerY] = "X"
            
            next = "Velha"
            
            os.system('clear') or None
            return playVoice(player, True, next, rp)
        
        else:
            os.system('clear') or None
            print("Valor inválido! \n \n")
                
            rp.text = text[5]
            rp.save(audio)
            playsound(audio)

            time.sleep(0.5)
            os.system('clear') or None 
            return playVoice(player, True, player)

    if (next == "Velha"):
        position_velhaX = random.randint(1, 3)
        position_velhaY = random.randint(1, 3)
            
        if(plane_game[position_velhaX][position_velhaY] == " "):
            plane_game[position_velhaX][position_velhaY] = "O"
            rp.text = f"Circulo na linha {position_velhaX}  na coluna {position_velhaY}"
            rp.save(audio)
            playsound(audio)
            next = player

        os.system('clear') or None        
        return playVoice(player, True, next, rp)
    
def started(player, rp):
    os.system('clear') or None
    number_sorted = random.randint(0, 10)

    rp.text = text[0]
    rp.save(audio)
    playsound(audio)

    number_player = float(input())

    os.system('clear') or None
    rp.text = f"Meu numero foi {number_sorted} e o seu foi {number_player}"
    rp.save(audio)
    playsound(audio)
    os.system('clear') or None

    if(number_player > 10 or number_player < 0):
        os.system('clear') or None
        print("Valor inválido! \n \n")

        rp.text = text[4]
        rp.save(audio)
        playsound(audio)
        time.sleep(0.5)
        start_game = "Velha"
        os.system('clear') or None   

    if(number_player > number_sorted):
        start_game = player
        rp.text = text[1]
        rp.save(audio)
        playsound(audio)

    elif(number_player < number_sorted):
        start_game = "Velha"
        rp.text = text[2]
        rp.save(audio)
        playsound(audio)

    else:
        rp.text = text[3]
        rp.save(audio)
        playsound(audio)
        time.sleep(0.5)
        return started(player, rp)
    
    time.sleep(0.5)
    os.system('clear') or None
    return start_game


def winner(player, plane_game):
    cont = 0
    
    if(plane_game[1][1] == "X" and plane_game[2][2] == "X" and plane_game[3][3] == "X" or plane_game[1][3] == "X" and plane_game[2][2] == "X" and plane_game[3][1] == "X"):
        return end(player, player)
    if(plane_game[1][1] == "O" and plane_game[2][2] == "O" and plane_game[3][3] == "O" or plane_game[1][3] == "O" and plane_game[2][2] == "O" and plane_game[3][1] == "O"):
        return end("Velha", player)

    for c in range(len(plane_game[0])):
        col = []
        for row in plane_game:
            col.append(row[c])
        if(col == [c, "X", "X", "X"]):
            return end(player, player)
            
        if(col == [c, "O", "O", "O"]):
            return end("Velha", player)
            
    
    for row in plane_game:
        if(row == [cont, "X", "X", "X"]):
            return end(player, player)
            
        if(row == [cont, "O", "O", "O"]):
            return end(player, player)
            
        cont += 1

def end(winner, player):
    if (winner == player):
        rp.text = text[6]
        rp.save(audio)
        playsound(audio)
        time.sleep(0.5)
        return "have_win"
    else:
        rp.text = text[7]
        rp.save(audio)
        playsound(audio)
        time.sleep(0.5)
        return "have_win"

audio = "audio.mp3"
language = "pt-br"
rp = gTTS(
    text    =   "a",
    lang    =   language
)
rp.save(audio)

playVoice(0, False, False, rp)
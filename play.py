import random, os, time

text = ["Informe um número de 0 a 10. \n",
        "Parabéns, pode começar! \n",
        "HAHAHAHAHAHA troxa, eu começo! \n",
        "Empatamos, vamos denovo! \n \n",
        "Opa, querendo quebrar as regras? \n Sua penalidade é perder a vez de começar. \n \n",
        "Opa, já está marcado, tente outro lugar meu jovem. \n",
        "Nããão eu fui derrotada, como?\n ... \n Você é algum tipo de Deus? \n De qualquer forma, foi um bom jogo, até nunca mais! \n",
        "AJOELHEM-SE DIANTE DE SUA DEUSA MÁQUINA \n"]

plane_game = [ " ", " ", " ",
               " ", " ", " ",
               " ", " ", " "]
def play(player, start, next):

    if is_winner(plane_game, player):
        for letter in text[7]:
            print(letter, end='', flush=True)
            time.sleep(0.1)
        return 0
    else:
        print("EMPATE LENDÁRIO")

    draw_board(plane_game)

    if not start:
        start = started(player)

        if(start == player):
            position_player = int(input("X na posição: "))

            if(plane_game[position_player-1] == " "):
                plane_game[position_player-1] = "X"
                next = "Velha"
                os.system('clear') or None
                return play(player, True, next)
            
            else:
                os.system('clear') or None
                print("Valor inválido! \n \n")
                
                for letter in text[4]:
                    print(letter, end='', flush=True)
                    time.sleep(0.1)
                time.sleep(0.5)
                start = "Velha"
                os.system('clear') or None    
        
        if (start == "Velha"):
            make_move(plane_game)
            next = player

            os.system('clear') or None        
            return play(player, True, next)
    
    if (next == player):
        position_player = int(input("X na posição: "))

        if(plane_game[position_player-1] == " "):
            plane_game[position_player-1] = "X"
            
            next = "Velha"
            
            os.system('clear') or None
            return play(player, True, next)
        
        else:
            os.system('clear') or None
            print("Valor inválido! \n \n")
                
            for letter in text[5]:
                print(letter, end='', flush=True)
                time.sleep(0.1)
            time.sleep(0.5)
            os.system('clear') or None 
            return play(player, True, player)

    if (next == "Velha"):
        make_move(plane_game)
        next = player

        os.system('clear') or None        
        return play(player, True, next)

def draw_board(plane_game):
    print(" " + plane_game[0] + " | " + plane_game[1] + " | " + plane_game[2])
    print("---+---+---")
    print(" " + plane_game[3] + " | " + plane_game[4] + " | " + plane_game[5])
    print("---+---+---")
    print(" " + plane_game[6] + " | " + plane_game[7] + " | " + plane_game[8])


def started(player):
    os.system('clear') or None
    number_sorted = random.randint(0, 10)

    for letter in text[0]:
        print(letter, end='', flush=True)

    number_player = float(input())

    os.system('clear') or None
    print(f"Sorteado: {number_sorted} \n Seu número: {number_player}")
    os.system('clear') or None

    if(number_player > 10 or number_player < 0):
        os.system('clear') or None
        print("Valor inválido! \n \n")

        for letter in text[4]:
            print(letter, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.5)
        start_game = "Velha"
        os.system('clear') or None   

    if(number_player > number_sorted):
        start_game = player
        for letter in text[1]:
            print(letter, end='', flush=True)
            time.sleep(0.1)

    elif(number_player < number_sorted):
        start_game = "Velha"
        for letter in text[2]:
            print(letter, end='', flush=True)
            time.sleep(0.1)

    else:
        for letter in text[3]:
            print(letter, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.5)
        return started(player)
    
    time.sleep(0.5)
    os.system('clear') or None
    return start_game

def is_draw(plane_game):
    return " " not in plane_game

def is_winner(plane_game, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]               # Diagonais
    ]
    for combination in winning_combinations:
        if plane_game[combination[0]] == plane_game[combination[1]] == plane_game[combination[2]] == player:
            return True
    return False

def minmax(plane_game, depth, is_maximizing_player, max_depth = 6):
    if depth >= max_depth:
        return 0
    
    if is_winner(plane_game, "X"):
        return -1
    
    elif is_winner(plane_game, "O"):
        return 1
    
    elif is_draw(plane_game):
        return 0
    
    if is_maximizing_player:
        max_eval = float("-inf")
        
        for i in range(9):
            if plane_game[i] == " ":
                plane_game[i] = "O"
                eval = minmax(plane_game, depth+1, False)
                plane_game[i]= " "
                max_eval = max(max_eval, eval)
        
        return max_eval
    
    else:
        min_eval = float("inf")
        for i in range(9):
            if plane_game[i] == " ":
                plane_game[i] = "X"
                eval = minmax(plane_game, depth+1, True)
                plane_game[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval
    
def make_move(plane_game):
    best_eval = float("-inf")
    best_move = None
    for i in range(9):
        if plane_game[i] == " ":
            plane_game[i] = "O"
            eval = minmax(plane_game, 0, False)
            plane_game[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    plane_game[best_move] = "O"


play("X", False, False)
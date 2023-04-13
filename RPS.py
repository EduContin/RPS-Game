import os # Importa lib para limpar o console
import random # Importa lib para usar random

# Variáveis
playerScore1 = 0
playerScore2 = 0
shouldContinue = True

# Clear console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# DEF cálculo de resultado da rodada
def gameCalc(play1, play2, playerScore1, playerScore2):

    # Código de empate
    if play1 == play2:
        return "0"

    # Código de Player1 SCORED
    elif (play1 == 1 and play2 == 3) or (play1 == 2 and play2 == 1) or (play1 == 3 and play2 == 2):
        return "1"

    # Código de Player2 SCORED
    elif (play1 == 1 and play2 == 2) or (play1 == 2 and play2 == 3) or (play1 == 3 and play2 == 1):
        return "2"

# Banner print
def banner():
    print(f"""
██████╗ ██████╗ ███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██████╔╝██████╔╝███████╗    ██║  ███╗███████║██╔████╔██║█████╗  
██╔══██╗██╔═══╝ ╚════██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║  ██║██║     ███████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚═╝     ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                
Dev: Eduardo S Contin, Fabricio G Pinterich, Enrico B R Santos, Gabriel Marques, Crystofer S D Dos Santos

SCOREBOARD --- PLAYER 1: {playerScore1} | PLAYER 2: {playerScore2} ---""")

# Cria lógica de MENU
while True:
    playerScore1 = 0
    playerScore2 = 0

    clear() # Limpa console
    banner() # Print banner

    # Print GAME OPTIONS
    print(
"""
SELECT GAME MODE:
[1] - PvP
[2] - PvAI
[3] - AIvAI
""")

    try:
        # Pede input do modo de jogo
        gameOption = int(input("Select your game (i.e: 1): "))

        if gameOption < 0 or gameOption > 3: # Se não for um modo jogável, reinicia
            continue
        
        # Seleção de Player VS Player
        if gameOption == 1:
            while True:
                clear() # Limpa console
                banner() # Print banner

                # Round do Player 1
                print("\n=-=-=-=-=-=-=-=-=-=\n  PLAYER 1 ROUND\n=-=-=-=-=-=-=-=-=-=")
                play1 = int(input("[1] Pedra\n[2] Papel\n[3] Tesoura\n\nDigite sua jogada: "))

                clear() # Limpa console
                banner() # Print banner

                # Round do Player 2
                print("\n=-=-=-=-=-=-=-=-=-=\n  PLAYER 2 ROUND\n=-=-=-=-=-=-=-=-=-=")
                play2 = int(input("[1] Pedra\n[2] Papel\n[3] Tesoura\n\nDigite sua jogada: "))
                    
                # Lógica de pontuação, envia dados dos players e verifica quem é o ganhador
                # Retorna "1" se Player1 ganhar, "2" se Player2

                resultado = gameCalc(play1, play2, playerScore1, playerScore2)

                if resultado == "1":
                    playerScore1 += 1
                    print("PLAYER 1 GANHOU!")
                elif resultado == "2":
                    playerScore2 += 1
                    print("PLAYER 2 GANHOU!")
                elif resultado == "0":
                    print("EMPATE!")

                shouldContinue = input("\nContinuar partida? (Y/n): ")

                if shouldContinue == "n":
                    break
                
        # Seleção de Player VS AI
        if gameOption == 2:
            while True:
                clear() # Limpa console
                banner() # Print banner

                # Round do Player 1
                print("\n=-=-=-=-=-=-=-=-=-=\n  PLAYER 1 ROUND\n=-=-=-=-=-=-=-=-=-=")
                play1 = int(input("[1] Pedra\n[2] Papel\n[3] Tesoura\n\nDigite sua jogada: "))

                clear() # Limpa console
                banner() # Print banner

                # Round da AI
                play2 = random.randint(1, 3)

                # Traduz resultado Play1 para texto 
                if play2 == 1:
                    playTraducao = "Pedra"
                elif play2 == 2:
                    playTraducao = "Papel"
                elif play2 == 3:
                    playTraducao = "Tesoura"

                print(f"\n=-=-=-=-=-=-=-=-=-=\n  BOT CHOOSED: {playTraducao} \n=-=-=-=-=-=-=-=-=-=\n")

                # Lógica de pontuação, envia dados dos players e verifica quem é o ganhador
                # Retorna "1" se Player1 ganhar, "2" se Player2

                resultado = gameCalc(play1, play2, playerScore1, playerScore2)

                if resultado == "1":
                    playerScore1 += 1
                    print("PLAYER 1 GANHOU!")
                elif resultado == "2":
                    playerScore2 += 1
                    print("PLAYER 2 GANHOU!")
                elif resultado == "0":
                    print("EMPATE!")

                shouldContinue = input("\nContinuar partida? (Y/n): ")

                if shouldContinue == "n":
                    break
            
        # Seleção de AI VS AI
        if gameOption == 3:
            while True:
                clear() # Limpa console
                banner() # Print banner

                # Round da AI 1
                play1 = random.randint(1, 3)

                # Traduz resultado Play1 para texto 
                if play1 == 1:
                    playTraducao = "Pedra"
                elif play1 == 2:
                    playTraducao = "Papel"
                elif play1 == 3:
                    playTraducao = "Tesoura"
                
                print(f"\n=-=-=-=-=-=-=-=-=-=\n  BOT 1 CHOOSED: {playTraducao} \n=-=-=-=-=-=-=-=-=-=")

                # Round da AI 2
                play2 = random.randint(1, 3)

                # Traduz resultado Play2 para texto 
                if play2 == 1:
                    playTraducao = "Pedra"
                elif play2 == 2:
                    playTraducao = "Papel"
                elif play2 == 3:
                    playTraducao = "Tesoura"
                print(f"\n=-=-=-=-=-=-=-=-=-=\n  BOT 2 CHOOSED: {playTraducao} \n=-=-=-=-=-=-=-=-=-=\n")

                # Lógica de pontuação, envia dados dos players e verifica quem é o ganhador
                # Retorna "1" se Player1 ganhar, "2" se Player2

                resultado = gameCalc(play1, play2, playerScore1, playerScore2)

                if resultado == "1":
                    playerScore1 += 1
                    print("PLAYER 1 GANHOU!")
                elif resultado == "2":
                    playerScore2 += 1
                    print("PLAYER 2 GANHOU!")
                elif resultado == "0":
                    print("EMPATE!")

                shouldContinue = input("\nContinuar partida? (Y/n): ")

                if shouldContinue == "n":
                    break

    except Exception as e:
        clear()
        banner()
        print(f"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nERROR! {e}\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        errorSkip = input("\nPressione qualquer tecla para continuar..")

#Foi definido que o tamanho da tela de jogo é de 20 linhas e 50 colunas. Delimitada por "*"
import os
from threading import Timer
import threading
semaphore = threading.Semaphore()
def threadScreen(playerPosition):
    linePlayer = playerPosition['line']
    columnPlayer = playerPosition['column']
    shoot = playerPosition['shoot']
    if(linePlayer > 19):
        linePlayer = 19
    if(linePlayer < 3):
        linePlayer = 3
    if(columnPlayer > 49):
        columnPlayer = 49
    if(columnPlayer < 3):
        columnPlayer = 3
    os.system('clear')
    semaphore.acquire()
    print('Instrucoes:\nu : up/para cima\nd : down/para baixo\nl : left/esquerda\nr : right/direita\ns: shoot/atira\n')
    for l in range(1, 21): 
        for c in range(1, 51):
# O caracter delimitador tem condicao diferente quando esta na coordenada correspondente ao jogador.
            if (l == 1 or l == 20 or c == 1 or (c == 50 and l !=linePlayer)): 
                print("*", end="")
            elif(l == linePlayer and c == 48):
                print("*", end="")
            elif(l == linePlayer and c == columnPlayer): # pro jogador aparecer l e c tem que ser maiores que 2
                print("\O/", end="")
            elif(shoot and l < linePlayer and c == columnPlayer):
               print("|", end ="")
            else : 
                print(" ", end="")
        print()
    semaphore.release()

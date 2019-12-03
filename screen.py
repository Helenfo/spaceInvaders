import os
import sys
from threading import Timer
import threading
from functions import initialValues
semaphore = threading.Semaphore()

def threadScreen(playerPosition, aliensPosition, obsPosition, message, shootNumber, fase):
    
    linePlayer = playerPosition['line']
    columnPlayer = playerPosition['column']
    shootPlayer = playerPosition['shoot']    
    
    lineAlien = aliensPosition['line']
    columnAlien = aliensPosition['column']
    shootAlien = aliensPosition['shoot']

    # flush na tela anterior
    os.system('clear')

    # inicio da atualizacao da tela
    semaphore.acquire()
    print('Instrucoes:\nu : up/para cima\nd : down/para baixo\nl : left/esquerda\nr : right/direita\ns: shoot/atira\nFASE', fase['number'])
    semaphore.release()

    # se for para uma nova fase, reinicia posicao dos componentes do jogo 
    if(message['new']):
       semaphore.acquire()
       fase['number'] = fase['number'] + 1
       message['new'] = False
       initialValues(playerPosition, aliensPosition, obsPosition, shootNumber, message, fase)

       linePlayer = playerPosition['line']
       columnPlayer = playerPosition['column']
       shootPlayer = playerPosition['shoot']
       
       lineAlien = aliensPosition['line']
       columnAlien = aliensPosition['column']
       shootAlien = aliensPosition['shoot']
       semaphore.release()

    if(message['over']):
        semaphore.acquire()
        os.system('clear')
        print('FIM DE JOGO')
        sys.exit()
        semaphore.release()

    semaphore.acquire()
    for l in range(1, 21): 
        for c in range(1, 51):
            # primeiro e analisado se a linha e coluna atuais sao as de delimitacao da tela de jogo
            if (l == 1 or l == 20 or c == 1 or (c == 50 and l != linePlayer and l != lineAlien)): 
                print("*", end = "")

            # a delimitacao da tela do jogo e diferente na linha que contem o jogador e o alien
            elif((l == linePlayer and c == 48) or (l == lineAlien and c == 48)):
                print("*", end = "")

            # posiciona o jogador
            elif(l == linePlayer and c == columnPlayer):
                print("\O/", end = "")
 
            # posiciona o alien -> criar funcao para os n aliens
            elif(l == lineAlien and c == columnAlien):
              print(".-.", end = "")

            # lanca tiro do jogador(para cima) e ou do alien(para baixo)
            elif((shootPlayer and l < linePlayer and l != lineAlien and c == columnPlayer) or (shootAlien and l > lineAlien and l != linePlayer and c == columnAlien)):
               print("|", end ="")

            # posiciona obstaculos
            elif((l == obsPosition['line1'] and c == obsPosition['column1']) or (l == obsPosition['line2'] and c == obsPosition['column2']) or (l == obsPosition['line3'] and c == obsPosition['column3']) or (l == obsPosition['line4'] and c == obsPosition['column4'])):
               print("(", end = "")
            elif((l == obsPosition['line1'] and c == obsPosition['column1'] + 1) or (l == obsPosition['line2'] and c == obsPosition['column2'] + 1) or (l == obsPosition['line3'] and c == obsPosition['column3'] + 1) or (l == obsPosition['line4'] and c == obsPosition['column4'] + 1)):
               print(")", end = "")
            elif((l == obsPosition['line1'] and c == obsPosition['column1'] + 2) or (l == obsPosition['line2'] and c == obsPosition['column2'] + 2) or (l == obsPosition['line3'] and c == obsPosition['column3'] + 2) or (l == obsPosition['line4'] and c == obsPosition['column4'] + 2)):
               print(")", end = "")

            # posicoes vazias   
            else : 
                print(" ", end = "")
        print()
    semaphore.release()

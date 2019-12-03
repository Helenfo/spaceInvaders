import keyboard
import threading
semaphore = threading.Semaphore()

def positionLine(playerPosition, line):
    if(line > 19):
        line = 19
    if(line < 2):
        line = 2
    playerPosition['line'] = line

def positionColumn(playerPosition, column):
    if(column > 49):
        column = 49
    if(column < 2):
        column = 2
    playerPosition['column'] = column

def obstBetween(obsPosition, aliensPosition, playerPosition, line, column):
    # verifica se tem obstaculo entre ele o jogador e o tiro
    if ((obsPosition[line] > playerPosition['line']) and (aliensPosition['line'] > obsPosition[line])):
        columnObstacle = aliensPosition['column'] - obsPosition[column]
        if(columnObstacle == 0 or columnObstacle == -2 or columnObstacle == -1):
            # obstaculo ta entre, logo o jogador  nao vai ser destruido
            return True
        else:
            return False
    else:
        return False

def threadPlayer(playerPosition, aliensPosition,message, obsPosition):
    while True:
        playerPosition['shoot'] = False
        columnShoot = aliensPosition['column'] - playerPosition['column']
        # tanto para este codigo de posicionamento do jogador quanto para o do alien, foi dada preferencia pra analise de tiro e depois para a atualizacao do posicionamento para que o alvo nao seja atingido com delay
        
        # se teve tiro
        if(aliensPosition['shoot']):
            semaphore.acquire()
            #verifica se existe um obstaculo entre o tiro e o jogador
            obst1 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line1', 'column1')
            obst2 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line2', 'column2')
            obst3 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line3', 'column3')
            obst4 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line4', 'column4')
            
            # verifica se o jogador vai ser destruido. Faixa do tiro - jogador ocupa 3 colunas
            if(not(obst1 and obst2 and obst3 and obst4) and (columnShoot == 0 or columnShoot == -2 or columnShoot == -1) and aliensPosition['line'] < playerPosition['line']):
                playerPosition['column'] = 2
                playerPosition['line'] = 2
                playerPosition['shoot'] = False
                message['over'] = True
                semaphore.release()
                break

            else:
                semaphore.release()
                break
        # se nao tiver tido tiro, atualiza a posicao do jogador
        if keyboard.is_pressed('l'):
            semaphore.acquire()
            column = playerPosition['column'] -1
            # valida valor da coluna de acordo com os limites da tela do jogo
            positionColumn(playerPosition, column)
            semaphore.release()
            break
        elif keyboard.is_pressed('r'):
            semaphore.acquire()
            column = playerPosition['column'] + 1
            positionColumn(playerPosition, column)
            semaphore.release()
            break
        elif keyboard.is_pressed('u'):
            # valida valor da linha de acordo com os limites da tela do jogo
            semaphore.acquire()
            line = playerPosition['line'] - 1
            positionLine(playerPosition, line)
            semaphore.release()
            break
        elif keyboard.is_pressed('d'):
            semaphore.acquire()
            line = playerPosition['line'] + 1
            positionLine(playerPosition, line)
            semaphore.release()
            break
        elif keyboard.is_pressed('s'):
            semaphore.acquire()
            playerPosition['shoot'] = True
            semaphore.release()
            break

import threading
import random
semaphore = threading.Semaphore()

def obstBetween(obsPosition, aliensPosition, playerPosition, line, column):
    # verifica se tem obstaculo entre ele o alien e o tiro
    if ((obsPosition[line] > aliensPosition['line']) and (playerPosition['line'] > obsPosition[line])):
        columnObstacle = playerPosition['column'] - obsPosition[column]
        if(columnObstacle == 0 or columnObstacle == -2 or columnObstacle == -1):
            # obstaculo ta entre, logo alien nao vai ser destruido
            return True
        else:
            return False
    else:
        return False


def threadAliens(aliensPosition, playerPosition, message, obsPosition, fase):
    while True:
        aliensPosition['shoot'] = False
        columnShoot = playerPosition['column'] - aliensPosition['column']

        #se teve tiro
        if(playerPosition['shoot']):
            semaphore.acquire()
            #verifica se existe um obstaculo entro o tiro e o alien
            obst1 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line1', 'column1')
            obst2 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line2', 'column2')
            obst3 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line3', 'column3')
            obst4 = obstBetween(obsPosition, aliensPosition, playerPosition, 'line4', 'column4')

            # verifica se o alien vai ser destruido. Faixa do tiro - alien ocupa 3 colunas
            if(not(obst1 and obst2 and obst3 and obst4) and (columnShoot == 0 or columnShoot == -2 or columnShoot == -1) and playerPosition['line'] > aliensPosition['line']):
                aliensPosition['column'] = 2
                aliensPosition['line'] = 2
                aliensPosition['shoot'] = False
                message['new'] = True
                semaphore.release()
                break

            else:
                semaphore.release()
                break

        # se nao tiver tido tiro, a cada atualizacao o alien muda de lugar
        else:
            semaphore.acquire()
            aliensPosition['column'] =  10#random.choice([4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46])
            aliensPosition['line'] =  10#random.choice([4,6,8,10,12,14,16,18])
            aliensPosition['shoot'] = random.choice([True, False])
            semaphore.release()
            break


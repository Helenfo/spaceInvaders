import random
import threading
semaphore = threading.Semaphore()

def verification(obsPosition, aliensPosition, shootNumber, column, line, obs):
   columnShootAlien = obsPosition[column] - aliensPosition['column']
   if(aliensPosition['shoot'] and (columnShootAlien == 0  or columnShootAlien == -2 or columnShootAlien == -1)):
       semaphore.acquire()
       shootNumber[obs] = shootNumber[obs] + 1
       semaphore.release()

def destroyObs(obsPosition, shootNumber, column, line, obs):
    if(shootNumber[obs] == 3):
     # obstaculo deve ser destruido
     semaphore.acquire()
     obsPosition[line] = 1 #posicao que nao e mostrada na tela
     obsPosition[column] = 1
     shootNumber[obs] == 0
     semaphore.release()

def threadScenario(aliensPosition, obsPosition, shootNumber):
    shootAlien = aliensPosition['shoot']
    lineAlien = aliensPosition['line']
    columnAlien = aliensPosition['column']
    while(1):
        # verifica se algum obstaculo foi atingido
        # faixa de tiro - obstaculo ocupa 3 colunas:
        verification(obsPosition, aliensPosition, shootNumber,'column1', 'line1', 'obs1')
        verification(obsPosition, aliensPosition, shootNumber,'column2', 'line2', 'obs2')
        verification(obsPosition, aliensPosition, shootNumber,'column3', 'line3', 'obs3')
        verification(obsPosition, aliensPosition, shootNumber,'column4', 'line4', 'obs4')

        # verifica se algum obstaculo foi atingido 3x e se vai ser destruido
        destroyObs(obsPosition, shootNumber, 'column1', 'line1', 'obs1')
        destroyObs(obsPosition, shootNumber,'column2', 'line2', 'obs2')
        destroyObs(obsPosition, shootNumber,'column3', 'line3', 'obs3')
        destroyObs(obsPosition, shootNumber,'column4', 'line4', 'obs4')
        break

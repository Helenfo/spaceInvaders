def initialValues(playerPosition, aliensPosition, obsPosition, shootNumber, message):
    playerPosition['line'] = 19
    playerPosition['column'] = 24
    playerPosition['shoot'] = False

    aliensPosition['line'] = [10,5,7]
    aliensPosition['column'] = [10,5,7]
    aliensPosition['shoot'] = [False,False,False]

    obsPosition['line1'] = 10
    obsPosition['column1'] = 30
    obsPosition['line2'] = 10
    obsPosition['column2'] = 40
    obsPosition['line3'] = 15
    obsPosition['column3'] = 7
    obsPosition['line4'] = 15
    obsPosition['column4'] = 10

    shootNumber['obs1'] = 0
    shootNumber['obs2'] = 0
    shootNumber['obs3'] = 0
    shootNumber['obs4'] = 0

    message['new'] = False
    message['over'] = False

def init():
    playerPosition = {'line' : 19, 'column' : 24, 'shoot' : False}
#    aliensPosition = {'line' : [10,5,7] 'column': [10,5,7], 'shoot' : [False,False,False]}
    aliensPosition = {'line' : 10, 'column' : 10, 'shoot' : False}
    obsPosition = {'line1' : 15, 'column1' : 8, 'line2' : 10, 'column2' : 40, 'line3' : 15, 'column3' : 30, 'line4' : 15, 'column4' : 15}
    shootNumber = {'obs1' : 0, 'obs2' : 0 , 'obs3': 0, 'obs4' : 0}
    message = {'new': False, 'over' : False}
    return playerPosition, aliensPosition, obsPosition, shootNumber, message

# limitar numero de fases


#colocar como reexecutar programa - no relatorio
# pensar se essas funcoes vao ficar aqui mesmo


#falta aumentar numero de inimigos
#falta fazer o logger

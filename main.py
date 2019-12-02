#libraries import
from multiprocessing import Process
from threading import Thread
from threading import Timer
import socket
import sys
import os
import time
import struct

#files import
from logger import loggerProcess
from player import threadPlayer
from aliens import threadAliens
from scenario import threadScenario
from screen import threadScreen

def mainProcess(name):
    print('i am the process',name)
    # time
    start_time = time.time()
    # create a UDP socket
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bint socket to a port
    #server_address = ('localhost', 10000)
    #sock.bind(server_address)
    i = -5
    playerPosition={'line':19, 'column':24, 'shoot':False}
    # cria todas as threads:
    while True:
        tScreen = Timer(0.1,threadScreen, args=(playerPosition,))# posicao inicial do jogador
        tPlayer = Thread(target=threadPlayer, args=(playerPosition,))
        tScreen.start()
        tPlayer.start()
        tScreen.join()
        #tPlayer.start()
    #tAliens = Thread(target=threadAliens, args=('aliens',))
    #tAliens.start()
    #tScenario = Thread(target=threadScenario, args=('scenario',))
    #tScenario.start()
    #tPlayer.join()

    # create the logger process
    #pLogger = Process(target=loggerProcess, args=('logger',))
    #pLogger.start()
    
#    fim = False
#    while isnotTrue:
#	Thread(target=threadScreen,    
#    data, address = sock.recvfrom(4096)
    #    print(data)
    #    elapsed_time = time.time() - start_time
        # olhar outros parâmetros que devem ser enviados ao logger
    #    i = i + 5
    #    print(round(elapsed_time,0))
    #    print(i)
    #    if(round(elapsed_time,0) == i):
    #        sent = sock.sendto(struct.pack('<1f',round(elapsed_time,2)), address)
     #       print('sent {} bytes back to {}'.format(sent, address))
            #i = 
    # criar lógica de finalização e criação dos processos e threads	
      #  fim = True
     #   pLogger.join() #join(timeout) -> the method blocks untils the process who called join terminates. If timeout is a positive number, it blocks at most timeout seconds. Check the process's exitcode to determine if it terminated
#    tPlayer.join()
    #tAliens.join()
    #tScenario.join()
    #tScreen.join()
if __name__ == '__main__':
    p = Process(target=mainProcess, args=('main',))
    p.start()
    p.join()

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
from functions import init
from logger import loggerProcess
from player import threadPlayer
from aliens import threadAliens
from scenario import threadScenario
from screen import threadScreen

def mainProcess(name):
    start_time = time.time()
    
    # UDP socket
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server_address = ('localhost', 10000)
    #sock.bind(server_address)
    i = -5

    #condicoes iniciais
    fase = {'number' : 0}
    playerPosition, aliensPosition, obsPosition, shootNumber, message = init()

    # cria todas as threads:
    while True:

        # cria processo Logger
        #pLogger = Process(target=loggerProcess, args=('logger',))
        #pLogger.start()
        #data, address = sock.recvfrom(4096)
        #print(data)
        #elapsed_time = time.time() - start_time
        #i = i + 5
        #print(round(elapsed_time,0))
        #if(round(elapsed_time,0) == i):
        #    sent = sock.sendto(struct.pack('<1f', round(elapsed_time,2)), address)
        #    print('sent {} bytes back to {}'.format(sent, address))
        #Timer(5,sent)

        tScreen = Timer(0.1,threadScreen, args=(playerPosition, aliensPosition, obsPosition,message,shootNumber,fase,))
        tPlayer = Thread(target = threadPlayer, args = (playerPosition,aliensPosition,message,obsPosition,))
        tScenario = Thread(target = threadScenario, args = (aliensPosition, obsPosition,shootNumber,))
        tAliens = Thread(target = threadAliens, args = (aliensPosition,playerPosition,message,obsPosition,fase,))
        tScreen.start()
        tPlayer.start()
        tAliens.start()
        tScenario.start()
        tScreen.join()
        tPlayer.join()
        tAliens.join()
        tScenario.join()
        #pLogger.join()
    
if __name__ == '__main__':
    p = Process(target=mainProcess, args=('main',))
    p.start()
    p.join()

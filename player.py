import keyboard
import threading
semaphore = threading.Semaphore()
def threadPlayer(playerPosition):
    while True:
        playerPosition['shoot'] = False
        if keyboard.is_pressed('l'):
            semaphore.acquire()
            playerPosition['column'] = playerPosition['column'] - 1
            semaphore.release()
            break
        elif keyboard.is_pressed('r'):
            semaphore.acquire()
            playerPosition['column'] = playerPosition['column'] + 1
            semaphore.release()
            break
        elif keyboard.is_pressed('u'):
            semaphore.acquire()
            playerPosition['line'] = playerPosition['line'] - 1
            semaphore.release()
            break
        elif keyboard.is_pressed('d'):
            semaphore.acquire()
            playerPosition['line'] = playerPosition['line'] + 1
            semaphore.release()
            break
        elif keyboard.is_pressed('s'):
            semaphore.acquire()
            playerPosition['shoot'] = True
            semaphore.release()
            break

import sys
import time


def loadingAnimation(process) :
    while process.isAlive() :
        chars = "/—\|" 
        for char in chars:
            sys.stdout.write('\r'+'Processing '+char)
            time.sleep(.1)
            sys.stdout.flush()

    print('\nDone.')
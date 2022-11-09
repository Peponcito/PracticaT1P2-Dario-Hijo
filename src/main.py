import os
from time import sleep

def padre():
    num = int(input("¿Cuántos procesos hijos quieres crear?: "))
    for i in range(num):
        newPid = os.fork()
        if newPid == 0:
            hijo()

def hijo():
    print("Soy el porceso HIJO con PID :  %d" % os.getpid())
    sleep(5)
    print("Muerto porceso hijo con PID : %d" %os.getpid())
    os._exit(0)

if __name__ == "__main__":
    padre()
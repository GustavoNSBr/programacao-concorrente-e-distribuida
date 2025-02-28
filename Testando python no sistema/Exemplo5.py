import threading
import time

#Variáveis globais

Contador = 0

lock = threading.Lock()

def Incrementar():
    global Contador
    for _ in range(1000):
        lock.acquire()
        Contador = Contador + 1
        lock.release()

tA = threading.Thread(target= Incrementar)
tB = threading.Thread(target= Incrementar)

tA.start()
tB.start()

tA.join()
tB.join()

print(f"Contador {Contador}")

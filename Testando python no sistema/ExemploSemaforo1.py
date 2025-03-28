import time
import threading

S = threading.Semaphore(3)

def trabalho(ID):
    print(f"Thread em execução: {ID} ")
    with S:
        print(f"Thread {ID} acessou o recurso.")
        threading.Event().wait(1)
    print(f"Thread {ID} liberou recurso." )

    threads = [threading.Thread(target = trabalho, args = (i, )) for i in range(5)]
    for t in threads: t.start()
    for t in threads: t.join
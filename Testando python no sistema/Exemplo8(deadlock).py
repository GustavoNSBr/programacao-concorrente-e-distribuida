import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def T1():
    print("T1: tentando adiquirir o lock1")
    lock1.acquire()
    print("T1: lock1 ok, tentando o lock2")
    time.sleep(1)
    lock2.acquire()
    print("T1: lock2 ok")
    lock2.release()
    lock1.release()
    print("T1: finalizado")

def T2():
    print("T2: tentando adiquirir o lock2")
    lock2.acquire()
    print("T2: lock2 ok, tentando o lock1")
    time.sleep(1)
    lock1.acquire()
    print("T2: lock1 ok")
    lock1.release()
    lock2.release()
    print("T2: finalizado")

t1 = threading.Thread(target= T1)
t2 = threading.Thread(target= T2)

t1.start()
t2.start()

t1.join()
t2.join()

# nunca vai ser executado enquanto nao quebrar o processo
print("Finalizando a execucao do código-fonte..") 
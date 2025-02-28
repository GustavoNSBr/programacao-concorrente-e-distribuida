import threading
import time

def tarefa():
    print("Início")
    time.sleep(4)
    print("Fim")

# tarefa()

T = threading.Thread(target=tarefa)
T.start()
T.join()    
print("Thread principal finalizada!")
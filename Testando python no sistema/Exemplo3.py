import threading
import time

def tarefa():
    print("Início")
    time.sleep(4)
    print("Fim")

# tarefa()

TA = threading.Thread(target=tarefa)
TB = threading.Thread(target=tarefa)
TA.start()
TA.join()    
TB.start()
TB.join()    
print("Thread principal finalizada!")
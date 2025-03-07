import threading
import time

Contador = 0

def incrementar():
    global Contador # Recurso compartilhado
    for _ in range(5000):
        ValorAtual = Contador
        time.sleep(0.00001)
        Contador = ValorAtual + 1

threads = []
for i in range(10):
    t = threading.Thread(target = incrementar)
    threads.append(t)
    t.start()

for k in threads:
    k.join()

print(f"Valor do contador: {Contador}")
import threading
import time

def Saudacao(nome, tempo):
    print(f"Olá, {nome}")
    time.sleep(tempo)
    print(f"Tchau, {nome}")

tA = threading.Thread(target= Saudacao, args= ("Ana", 5))
tB = threading.Thread(target= Saudacao, args= ("Bratriz", 2))

# tA e tB executam paralelamente!!!

tA.start()
tB.start()

# A e B nao dependem um do outro neste caso pois foram executados "simultaneamente"

tA.join() # Fica verificando se A terminou para executar a próxima linha
tB.join() # Fica verificando se B terminou para executar a próxima linha



print("Thread principal finalizada!")
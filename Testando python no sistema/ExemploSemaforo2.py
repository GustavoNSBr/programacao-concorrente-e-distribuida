import threading

B = threading.Barrier(3)

def trabalho(ID):
    print(f"Thread {ID} em execução.")
    threading.Event().wait(1)
    print(f"Thread {ID} chegou na barreira.")
    B.wait()
    print(f"Thread {ID} passou da barreira.")

threads = [threading.Thread(target= trabalho, args=(i, ))for i in range(6)]
for t in threads: t.start()
for t in threads: t.join()
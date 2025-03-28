import random
import time
import threading

# Função principal do QuickSort

def quicksort_naoparalelo(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô
    return quicksort_naoparalelo(left) + [pivot] + quicksort_naoparalelo(right)

# versao paralela

def quicksort_paralelo(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô

    ListaEsquerda = []
    ListaDireita = []

    def OrdernarEsquerda():
        nonlocal ListaEsquerda
        ListaEsquerda.extends(quicksort_paralelo(left))

    def OrdernarDireita():
        nonlocal ListaDireita
        ListaDireita.extends(quicksort_paralelo(right))

    left_thread = threading.Thread(target = OrdernarEsquerda)
    right_thread = threading.Thread(target = OrdernarDireita)

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return quicksort_paralelo(left) + [pivot] + quicksort_paralelo(right)

# Função para gerar números aleatórios

def gerar_numeros_aleatorios(n=10000, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]


if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()

# Função principal para testar o QuickSort nao paralelo

    print("Primeiros 10 números antes da ordenação:", numeros)
    t0 = time.time()
    numeros_ordenados = quicksort_naoparalelo(numeros)    
    tf = time.time()
    print(f"Tempo de execução (nao_paralelo): {tf - t0:.4f} seg")
    print("Primeiros 10 números após a ordenação:", numeros_ordenados)


# Função principal para testar o QuickSort paralelo

    print("Primeiros 10 números antes da ordenação:", numeros)
    t0 = time.time()
    numeros_ordenados = quicksort_paralelo(numeros)    
    tf = time.time()
    print(f"Tempo de execução (paralelo): {tf - t0:.4f} seg")
    print("Primeiros 10 números após a ordenação:", numeros_ordenados)
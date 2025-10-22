# --- BÚSQUEDA BINARIA ---
# El programa busca un número dentro de una lista ordenada dividiéndola a la mitad cada vez

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2  # posición media
        if lista[mitad] == objetivo:
            return mitad  # se encontró el número
        elif lista[mitad] < objetivo:
            inicio = mitad + 1  # buscar en la mitad derecha
        else:
            fin = mitad - 1  # buscar en la mitad izquierda
    return -1  # si no se encuentra

n = int(input("Cantidad de números en la lista: "))
numeros = []
for _ in range(n):
    num = int(input("Ingrese un número: "))
    numeros.append(num)
numeros.sort()  # primero se ordena la lista
print("Lista ordenada:", numeros)

valor = int(input("Número a buscar: "))
pos = busqueda_binaria(numeros, valor)
if pos != -1:
    print(f"El número {valor} está en la posición {pos}")
else:
    print("El número no se encontró")

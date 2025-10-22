# ==========================================================
# Programa hecho por Luis Bordeth
# Encuentra la mediana de una lista y muestra el doble de ella
# ==========================================================

# --- Paso 1: leer el tamaño de la lista ---
n = int(input("Ingrese el tamaño de la lista: "))

# --- Paso 2: leer los elementos ---
lista = []
for i in range(n):
    num = float(input(f"Ingrese el elemento {i+1}: "))
    lista.append(num)

# --- Paso 3: ordenar la lista de menor a mayor ---
lista.sort()

print("\nLista ordenada:", lista)

# --- Paso 4: calcular la mediana ---
if n % 2 == 1:
    # Si el tamaño es impar, la mediana es el elemento del medio
    mediana = lista[n // 2]
else:
    # Si es par, la mediana es el promedio de los dos centrales
    mediana = (lista[n // 2 - 1] + lista[n // 2]) / 2

# --- Paso 5: imprimir la mediana y su doble ---
print("Mediana:", mediana)
print("Doble de la mediana:", 2 * mediana)

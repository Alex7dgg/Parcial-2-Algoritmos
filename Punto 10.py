# ==========================================================
# Programa hecho por Luis Bordeth
# Determina si una matriz 3x3 es triangular o no
# ==========================================================

# --- Paso 1: ingresar los elementos de la matriz 3x3 ---
matriz = []
print("Ingrese los elementos de la matriz 3x3:")

for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

# --- Paso 2: mostrar la matriz ---
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# --- Paso 3: verificar si es triangular superior ---
# (Todos los elementos por debajo de la diagonal son 0)
es_superior = True
for i in range(3):
    for j in range(i):
        if matriz[i][j] != 0:
            es_superior = False

# --- Paso 4: verificar si es triangular inferior ---
# (Todos los elementos por encima de la diagonal son 0)
es_inferior = True
for i in range(3):
    for j in range(i + 1, 3):
        if matriz[i][j] != 0:
            es_inferior = False

# --- Paso 5: determinar el tipo de matriz ---
if es_superior and not es_inferior:
    print("\nLa matriz es TRIANGULAR SUPERIOR.")
elif es_inferior and not es_superior:
    print("\nLa matriz es TRIANGULAR INFERIOR.")
elif es_inferior and es_superior:
    print("\nLa matriz es DIAGONAL (todos los fuera de la diagonal son 0).")
else:
    print("\nLa matriz NO es triangular.")

# ==========================================================
# Programa hecho por Luis Bordeth - Problema "Caín y Abel"
# Acepta el reto #111
# ==========================================================

# Calcula el área bajo un polinomio f(x) usando el método de los rectángulos
def area_polinomio(coef, n):
    h = 1.0 / n       # ancho de cada rectángulo
    area = 0.0
    for i in range(n):
        x = i * h     # punto inicial de cada rectángulo
        fx = 0.0
        # Evaluar el polinomio en x
        for c in coef:
            fx = fx * x + c
        area += fx * h  # área del rectángulo
    return area

# --- Programa principal ---
while True:
    datos = input().strip().split()
    if not datos:
        break

    grado = int(datos[0])
    if grado == 20:   # fin del programa
        break

    # Leer coeficientes y número de rectángulos
    coef = list(map(float, datos[1:-1]))
    n = int(datos[-1])

    # Calcular el área bajo f(x)
    area = area_polinomio(coef, n)

    # La tierra total mide 1x1 hectómetro cuadrado
    area_total = 1.0
    area_abel = area_total - area
    dif = abs(area - area_abel)

    # Comparar resultados
    if dif <= 0.001:
        print("JUSTO")
    elif area > area_abel:
        print("CAIN")
    else:
        print("ABEL")

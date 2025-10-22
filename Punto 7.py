# ==========================================================
# Programa hecho por Luis Bordeth
# Conjugador de verbos regulares en distintos tiempos
# A = pasado (pretérito imperfecto)
# P = pretérito perfecto simple
# F = futuro
# t = terminar programa
# ==========================================================

def conjugar(verbo, tiempo):
    """
    Función que recibe un verbo (infinitivo) y una letra que indica el tiempo:
    A = pasado, P = pretérito perfecto, F = futuro
    Retorna una lista con las conjugaciones del verbo.
    """

    # Terminaciones regulares
    terminacion = verbo[-2:]   # ar, er o ir
    raiz = verbo[:-2]          # parte del verbo sin la terminación

    # --- Definimos terminaciones por tiempo ---
    if tiempo == 'A':  # pasado (imperfecto)
        if terminacion == "ar":
            sufijos = ["aba", "abas", "aba", "ábamos", "abais", "aban"]
        else:  # er o ir
            sufijos = ["ía", "ías", "ía", "íamos", "íais", "ían"]

    elif tiempo == 'P':  # pretérito perfecto simple
        if terminacion == "ar":
            sufijos = ["é", "aste", "ó", "amos", "asteis", "aron"]
        else:
            sufijos = ["í", "iste", "ió", "imos", "isteis", "ieron"]

    elif tiempo == 'F':  # futuro
        sufijos = ["é", "ás", "á", "emos", "éis", "án"]

    else:
        return None  # si el tiempo no es válido

    # --- Personas gramaticales ---
    personas = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]

    # --- Construimos las conjugaciones ---
    conjugaciones = []
    for p, suf in zip(personas, sufijos):
        if tiempo == 'F':
            verbo_conjugado = verbo + suf  # futuro se añade al infinitivo
        else:
            verbo_conjugado = raiz + suf   # otros se añaden a la raíz
        conjugaciones.append(f"{p} {verbo_conjugado}")

    return conjugaciones


# --- Programa principal ---
print("=== CONJUGADOR DE VERBOS REGULARES ===")
print("A = pasado, P = pretérito perfecto, F = futuro, t = terminar")

while True:
    verbo = input("\nIntroduce un verbo (o 't' para salir): ").strip().lower()

    if verbo == 't':  # salir del programa
        print("Programa terminado.")
        break

    tiempo = input("Introduce el tiempo (A, P o F): ").strip().upper()

    resultado = conjugar(verbo, tiempo)

    if resultado:
        print("\nConjugación del verbo:", verbo)
        for forma in resultado:
            print(forma)
    else:
        print("Tiempo no válido o verbo irregular.")

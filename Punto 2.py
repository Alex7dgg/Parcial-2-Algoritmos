Letras = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Frase = str(input('Escriba una frase: ')).upper().strip()
NovaFrase = ''
for letra in Frase:
    if letra in Letras:
        NovaFrase += Letras[(Letras.index(letra) + 3) % 26]
    else:
        NovaFrase += letra
print(NovaFrase)
def entero_a_romano(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    romano = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            romano += syms[i]
            num -= val[i]
        i += 1
    return romano
n = 1
while n != 0:
    n = int(input("Ingrese un número entero: "))
    print(entero_a_romano(n))
else:
    print("Número fuera de rango.")
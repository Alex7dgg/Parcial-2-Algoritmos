nlist = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]
n = int(input("Ingrese un número entero: "))
nNova = []
for i in range(len(nlist) + 1):
    for j in range(i+1, len(nlist)):
        Sum = nlist[i] + nlist[j]
        if Sum ==n:
            nNova.append((nlist[i], nlist[j]))
print(nNova)
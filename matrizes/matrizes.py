matriz = [[]]
for i in range(0, 3, 1):
    linha = []
    for j in range(0, 3, 1):
        elemento = int(input("digite um valor [%d][%d]:"%(i, j)))
        linha.append(elemento)
    matriz.append(linha)
print(matriz)
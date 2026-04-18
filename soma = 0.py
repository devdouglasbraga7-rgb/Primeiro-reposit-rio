contador_maior_10 = 0
soma = 0
media = 0

for i in range(5):
    numeros = int(input("digite um numero: "))
    if numeros > 10:
        contador_maior_10 += 1
    soma += numeros
    media = (soma)/5
    
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
print(f"A quantidade de números que são maiores que 10 é: {contador_maior_10}")
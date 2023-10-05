numeros = [0] * 30
for x in range(30):
    numeros[x] = int(input('Digite um número: '))

quantidade = 0
num = int(input('Digite o número a ser pesquisado: '))
for y in range(30):
    if num == numeros[y]:
        quantidade += 1

print(f'O número {num} aparece {quantidade} vezes na lista')
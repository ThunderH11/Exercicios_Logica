num = [0] * 30
qtd_pares = 0
soma = 0

for x in range(30):
    num[x] = int(input('Digite um número: '))

maior = num[0]
menor = num[0]
for y in range(30):
    if num[y] % 2 == 0:
        qtd_pares += 1

    soma += num[y]

    if num[y] > maior:
        maior = num[y]
    if num[y] < menor:
        menor = num[y]

media = soma / 30
qtd_media = 0

pares = [0] * qtd_pares
for z in range(30):
    indice_pares = 0
    if num[z] % 2 == 0:
        pares[indice_pares] = num[z]
        indice_pares += 1

    if num[z] > media:
        qtd_media += 1

print(f'Os números pares são: {pares}')
print(f'O maior valor é {maior} e o menor é {menor}')
print(f'A quantidade de números acima da média é {qtd_media}')
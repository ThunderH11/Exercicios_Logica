nome = [0,0,0,0,0]
senha = [0,0,0,0,0]

for x in range(5):
    nome[x] = input("Digite o nome do usuário: ")
    senha[x] = input("Digite a senha do usuário: ")

for y in range(5):
    print(f'Posição:{y}  Usuário: {nome[y]}  Senha: {senha[y]}')
print("----------------- Pedra Papel ou Tesoura -----------------")
elemento1=input("digite um dos 3 elementos")
elemento2=input("digite um dos 3 elementos")

if elemento1 == 'pedra '  'PEDRA'  and elemento2 == 'tesoura' :
    print('Pedra ganhou')
elif elemento1 == 'pedra '  'PEDRA'  and elemento2 == 'PAPEL':
    print("papel ganhou")

if elemento1 == 'tesoura '  and elemento2 == 'papel' :
    print('tesoura ganhou')
elif elemento1 == 'tesoura'  and elemento2 == 'pedra':
    print("pedra ganou")


if elemento1 == 'papel '  and elemento2 == 'pedra' :
    print('papel ganhou')
elif elemento1 == 'papel'  and elemento2 == 'tesoura':
    print("Tesoura ganou")

elif elemento1==elemento2:
    print("empete")



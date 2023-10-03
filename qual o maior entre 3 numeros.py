x='s'
while x == 's':

    numero1=int(input("digite sua idade"))
    mes=int(input("digite o mes que voce nasceu?"))
    if mes >=9:
        numero1=numero1+1
    anoNasc=2023-numero1
    print(anoNasc)
    x = input("voce quer digitar outra idade?")

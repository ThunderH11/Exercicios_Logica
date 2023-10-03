numero1 = int(input("digite a altura do triangulo"))
numero2 = int(input("digite o tamanho da base do triangulo"))
while numero1 <= 0 :
    print('nao pode 0 \n')
    numero1 = int(input("digite a altura do triangulo"))
while numero2 ==0:
    print('nao pode 0 \n')
    numero2 = int(input("digite o tamanho da base do triangulo"))
area=(numero1*numero2)/2
print("nao aceitamos 0", area)




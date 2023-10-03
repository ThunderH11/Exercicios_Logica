resposta='s'
while resposta =='s':
    numero = int(input("digite um numero"))
    while numero == 0:
        numero = int(input("digite um numero direfente de 0"))
    if numero > 0:
        print("numero positivo")
    else:
        print("negativo")
        
    resposta=input("quer repetir")






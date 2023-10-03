nulos=int(input("digite o numero de nulos"))
validos=int(input("digite o numero de validos"))
brancos=int(input("digite o numero de brancos"))
somatotal=nulos+validos+brancos
ponulo=(nulos/somatotal)*100
povalido=(validos /somatotal)*100
pobranco=(brancos/somatotal)*100
print(somatotal)
print("quantos porcento de votos nulos",ponulo)
print("quantos porcento de votos valido",povalido)
print("quantos porcento de votos branco",pobranco)
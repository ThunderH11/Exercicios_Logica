numero=int(input("digite a quantidades que voce quer armazenar"))
caixa1=[0]*numero
caixa2=[0]*numero
soma=[0]*numero
for x in range (numero):
    caixa1[x]=int(input(f"digite o{x+1}"))
    caixa2[x]=int(input(f"digite o{x+1}"))
    soma[x]=caixa1[x]+caixa2[x]

print(caixa1)
print(caixa2)
print(soma)


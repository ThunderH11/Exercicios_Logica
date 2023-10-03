x='s'
while x == 's':
    soma= 0
    media= 0
    quantos=int(input("quantos numeros voce quer digitar"))
    for x in range(0,quantos,1):
        nota=int(input(f"digite a {x+1} nota"))
        soma=soma+nota
    media=soma/quantos
    print(soma)
    print(media)
    x=input("quer repetir?")
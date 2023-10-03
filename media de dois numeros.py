x='s'
while x=='s':
    numero1=(float(input("Digite a primeira nota")))
    numero2=float(input("Digite a primeira nota"))
    media=(numero1+numero2)/2
    print("essa é a media do aluno",media)
    if media >= 7:
        print("aprovado")
    elif media>=4 :
        print("recuperaçao")
    else:
        print("foto com o professor")
    if x=='s':
       x=input("quer repetir")
    else:
        break
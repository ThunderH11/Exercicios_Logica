while True:
    x=int(input("digite o numero"))
    repetir=int(input("digite 1 para sucessor , 2 para antecessor e 3 para finalizar "))
    if repetir == 1:
        print("esse é o numero sucessor" , x+1)
    elif repetir == 2:
        print("esse é o numero antecessor" , x-1)
    elif repetir == 3:
        break
    else:
        print("opcao invalida")



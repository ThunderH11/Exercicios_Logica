repetir = 's'
while repetir == 's':

    numero = int(input("digite um numero     \n"))
    if numero % 2 == 0:
        print("esse numero é par \n")
    else:
        print("esse numer é impar\n")

    repetir=input(" quer repetir?")
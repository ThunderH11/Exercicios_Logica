print("=-=-" * 4, "Jogo da Forca", "-=-=" * 4)
a = ["a", "m", "o", "r"]

vidas = 5
letraX = [" "] * 10

for X in range(10):
    print(" ")
    letraX[X] = input("Digite uma letra: ")
    print(" ")

    if letraX[X] in a:
        print("Você acertou uma letra")
        print(" ")
        a.remove(letraX[X])  
    else:
       vidas = vidas - 1
       print(f"Você perdeu uma vida \nVocê tem: {vidas} vidas")
       print(" ")
    if vidas==4:
      print(" |----")                                
      print(" ")
    elif vidas==3:
      print(" |----")
      print(" |   O")
      print(" ")
    elif vidas==2:
      print(" |----")  
      print(" |   O")
      print(" |  /|\\")
      print(" ")
    elif vidas == 1:
      print(" |----")  
      print(" |   O")
      print(" |  /|\\")
      print(" |  / \\")  
      print(" ")
    elif vidas==0:
      print("=-=-= " * 8)
      print(" ")
      print(" !!! Você Morreu !!!")
      print(" |----")  
      print(" |   O")
      print(" |  /|\\")
      print("| / \\")  
      print(" ")
      print(" Morreu krl")
      print("=-=-= " * 8)
      break

    if len(a) == 0:
        print(f"Você ficou com {vidas}")
        print(" ")
        print("Parabéns! Você ganhou!")
        break
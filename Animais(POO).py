class animal:
    def _init_(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def som(self):
        print(f"O {self.nome} esta emitindo som")

class gato(animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def som(self):
        print((f" O esta {self.nome} esta miando"))

class cachoro(animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def som(self):
        print(f" O {self.nome} esta latindo ")


class coelho (animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def som(self):
        print(f"O {self.nome} esta ?? nao sei o barulho")

class vaca(animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def som(self):
        print(f"a {self.nome} esta murmurando")


# sem utilizar o import para deixar tudo em um arquio

joao = animal("curupira","branco")
print(f"{joao.nome} {joao.cor}")

mike = gato("mike","preto")
mike.som()

mila = cachoro("mila","branca")
mila.som()

kinho = coelho("kizinh","roxo")
kinho.som()

zinho = vaca("mimoza","preto e branco")
zinho.som()
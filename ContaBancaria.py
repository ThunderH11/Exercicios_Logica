class ContaBancaria:
    def __init__(self, numero, saldo, nome, tipo, limite, status=False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.status = status

    def verificarsaldo(self):
        print(f"Saldo: R$ {self.saldo}")

    def statuss(self):
        if self.status == True:
            print("Sua conta está ativa")
        else:
            print("Sua conta não está ativa")

    def limitee(self):
        limite =  8000
        print(f"seu limite é de: R${limite}")

    def depositaa(self,depositar):
        self.saldo = self.saldo + depositar
        print(f"você recebeu um deposito de: {depositar} e esta com {self.saldo}")

    def saquee(self,sacar):
        self.saldo = self.saldo - sacar
        print(f"voce sacou: R${sacar} e esta com {self.saldo}")


tanus = ContaBancaria(numero=3431, saldo=2200, nome="tanus", tipo="corrente", limite=1, status=True)
print(f"Numero da conta:{tanus.numero} , Nome do usuario:{tanus.nome} Saldo:{tanus.saldo} Tipo da conta:{tanus.tipo} limite :{tanus.limite} {tanus.status}")
tanus.verificarsaldo()
tanus.statuss()
tanus.depositaa(800)
tanus.limitee()
tanus.saquee(12)
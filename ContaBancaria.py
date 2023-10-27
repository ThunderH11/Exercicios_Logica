class ContaBancaria:
    def __init__(self, numero, saldo, nome, tipo, limite, status=False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.status = status
        self.depositar = 900
    def verificarsaldo(self):
        print(f"Saldo: R$ {self.saldo}")

    def ativar(self):
        if self.status == True:
            print("Sua conta está ativa")
        else:
            print("Sua conta não está ativa")

    def limi(self):
        self.limite = self.saldo + 600 
        print(f"seu limite é de: R${self.limite}")

    def depo(self):
        self.depositar = self.saldo 
        print(f"valor depositado na sua conta {self.saldo}") 

tanus = ContaBancaria(numero=3431, saldo=2200, nome="tanus", tipo="corrente", limite=7, status=True)
print(f"Numero da conta:{tanus.numero} , Nome do usuario:{tanus.nome} Saldo:{tanus.saldo} Tipo da conta:{tanus.tipo} limite :{tanus.limite} {tanus.status}")
tanus.verificarsaldo()
tanus.ativar()
tanus.limi()
tanus.depo()






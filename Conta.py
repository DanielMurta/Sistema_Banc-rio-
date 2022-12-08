from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, senha, saldo):
        self.agencia = agencia
        self.senha = senha
        self.saldo = saldo

    def Depositar(self, valor):
        self.saldo += valor

    def Informacoes(self):
        print(f'Agência: {self.agencia}')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor





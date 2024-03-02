class Conta:
    def __init__(self, numero: str, saldo: float) -> None:
        self.numero = numero
        self.saldo = saldo

    def  __str__(self) -> str:
        return f"Conta {self.numero}: R${self.saldo: .2f}"
    
    def depositar(self, valor: float) -> None:
        self.saldo += valor
        print(f"Saldo {self.saldo}")

    def sacar(self, valor:float) -> None:
        try:
            if valor > self.saldo:
                raise ValueError ("Saldo insuficiente - Saque")
            self.saldo -= valor
        except ValueError:
            print(f"Erro ao sacar. Classe: {self.__class__.__name__}, Método: {self.sacar.__name__}")


class contaCorrente(Conta):
    def __init__(self, numero: str, saldo: float, limite) -> None:
        super().__init__(numero, saldo)
        self.limite = limite

    def sacar(self,valor:float):
        try:
            if valor > self.saldo:
                raise ValueError ("Saldo insuficiente - Saque")
            self.saldo -= valor
        except ValueError:
            print(f"Erro ao sacar. Classe: {self.__class__.__name__}, Método: {self.sacar.__name__}")

contaNova = Conta("1234",55)
contaNova.depositar(valor=100.00)
contaNova.depositar(100.00)
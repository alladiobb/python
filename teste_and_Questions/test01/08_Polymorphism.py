class Conta:
    def __init__(self, numero: str, saldo: float) -> None:
        self.numero = numero
        self.saldo = saldo

    def  __str__(self) -> str:
        return f"Conta {self.numero}: R${self.saldo: .2f}"
    
    def depositar(self, valor: float):
        saldo += valor

    def sacar(self,valor:float):
        try:
            if valor > self.saldo:
                raise ValueError ("Saldo insuficiente - Saque")
            saldo -= valor
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
            saldo -= valor
        except ValueError:
            print(f"Erro ao sacar. Classe: {self.__class__.__name__}, Método: {self.sacar.__name__}")
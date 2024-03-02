class MinhaExcecaoPersonalizada(Exception):
    def __init__(self, mensagem: str, *args: object) -> None:
        self.mensagem = mensagem
        super().__init__(*args)

def dividir(x: float, y: float):
    if y == 0:
        raise MinhaExcecaoPersonalizada("Não é possível dividir por zero!")
    return x / y

try:
    resultado = dividir(0,1)
except MinhaExcecaoPersonalizada as e:
    print("Erro: ", e.mensagem)
else:
    print("Resultado", resultado)

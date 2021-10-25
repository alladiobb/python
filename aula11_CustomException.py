#Obrigatóriamente você necessita fazer essas quatro linhas abaixo:
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x=int(input("Entre com um número de 0 a 10:"))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser MAIOR que 10!')
        if x < 0:
            raise InputError('Nota não pode ser MENOR que 10!')
        break
    except ValueError:
        print("Valor inválido. Entre com um número de 0 a 10:")
    except InputError as ex:
        print(ex)

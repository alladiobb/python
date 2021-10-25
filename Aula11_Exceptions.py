lista = [1,10]


try:
    divisao=10/1
    numero = lista[1]
    x=a
except ZeroDivisionError:
    print("Erro na divisão por 0 - Não é possível executar essa operação!")
except IndexError:
    print("Erro ao acessar uma posição - Não é possível executar essa operação!")
except BaseException as ex:
    print('Erro desconhecido. Erro:{}'.format(ex))
else:
    print("Código funcionou sem erro algum!")
finally:
    print("Dando erro ou não SEMPRE ira executar essa linha")
    
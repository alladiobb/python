

#Exemplo anterior sobre impressão
# for x in range (1, a+1):
#     resto = a%x
#
#     # print('Soma:{soma} \nSubtracao:{subtracao}'.format(soma=soma,subtracao=subtracao))
#     resultado = ('Valor de a :{}'
#                  '\n Valor de x = {}'
#                  '\n Resto = {} )'.format(a,x,resto))
#     print(resultado)

# Imprime se o numero selecionado é primo ou não
# a = int (input("Digite um número inteiro para verificar se é primo:"))
# div = 0
# for x in range (1, a+1):
#     resto = a%x
#     print(a, x, resto)
#     if resto ==0:
#         div +=1
#
# if div ==2:
#     print('numero {} é primo'.format(a))
# else:
#     print('numero {} não é primo'.format(a))


# Imprime os primos de 1 até o número escolhido
# num = int (input("Digite o até que número você quer saber se é primo:"))
# for num in range (115):
#     div = 0
#     for x in range (1, 115):
#         resto = num%x
#         # print(a, x, resto)
#         if resto ==0:
#             div +=1
#     if div ==2:
#         print('numero {} é primo'.format(num))

a= 0
while a<10:
    print(a)
    a+=1
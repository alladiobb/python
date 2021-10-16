listaPalavras = ['um','dois','três']

def contador_letras(listaPalavras):
    contador = []
    for x in listaPalavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

print(contador_letras(listaPalavras))

#Teste
print(len('um'))

contadorLetrasLambda = lambda listaLam:[len(x) for x in listaLam]

print(contadorLetrasLambda(listaPalavras))

soma = lambda a,b:a+b
subtracao = lambda a,b:a-b

print(soma(10,15))

calculadora = {
    'soma':lambda a,b:a+b,
    'sub':lambda a,b:a-b,
    'mult':lambda a,b:a*b,
    'divisao':lambda a,b:a/b
}
soma = calculadora['soma']

print(soma(10,5))
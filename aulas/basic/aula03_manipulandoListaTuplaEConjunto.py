animais=['papagaio','gato','cachorro']

animais.remove('gato')
animais.append('papagaio_novo')
#animais.append(['papagaio_velho','tatu'])

animais.extend(['papagaio_velho','tatu'])

print(animais)
print(len(animais))

print('---VALORES---')
valores = [1,2,3, 50, 100,-25,-3,-1,-2]

print(min(valores))
print(max(valores))
valores.sort()
print(valores)

#TUPLAS

tp = ['banana','maça',10,50]

print(tp[0])
print(tp.count('maça'))
print(tp[0:3])

#DICIONÁRIO {}

dc = {'maça':10,'uva':15,'pera':35}
print(dc["maça"])
print(dc)
#LISTA
#Criando, Adicionando, Imprimindo
lista = []
lista.append(1)
lista.append('Alladio')
lista.append(3.14)
print(lista)

#remove ultimo elemento
lista.pop()
print(lista)

#colocando ultimo elemento retirado
lista.append(3.14)
print(lista)

#Removendo um elemento especifico
lista.remove('Alladio')
print(lista)

#para inserir mais de um elemento
lista.extend([3,4])
print(lista)

#diminuindo o tamanho da lista. 
#[2:4] -> Siginifica: Exclua do 2 ao 4
del lista[2:4]
print(lista)
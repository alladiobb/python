
def dividir_lista(lista):

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    return esquerda, direita

def merge_sort(lista):
    """
    Função para ordenar a lista usando o algoritmo Merge Sort.

    Argumentos:
        lista: A lista a ser ordenada.

    Retorna:
        A lista ordenada.
    """

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    print(esquerda, direita)
    return merge(esquerda, direita)

def merge(esquerda, direita):
    """
        Função para mesclar duas listas ordenadas em uma única lista ordenada.

        Argumentos:
            esquerda: A primeira lista ordenada.
            direita: A segunda lista ordenada.

        Retorna:
            A lista ordenada resultante da mesclagem das duas listas.
    """

    resultado = []
    #Variaveis para acompanhar os Indices das listas 
    i = 0
    j = 0
    #Verifica se os indices das lista não são menores que o tamanho das litas
    while i < len(esquerda) and j < len(direita):
        #Vai comparando as duas e colocando os numeros em ordem crescente 
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    #Coloca os elementos remanescentes que não foram contabilizados acima
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado



# Exemplo de uso
lista = [ 7, 2, 4, 1, 3, 5 , 6]
print(f"Lista original: {lista}")

lista_ordenada = merge_sort(lista)
print(f"Lista ordenada: {lista_ordenada}")

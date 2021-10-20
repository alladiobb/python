# 'w' -> Escreve em um arquivo OBS: Limpa o que já tem
# 'a' -> Adiciona ao arquivo existente

def escreverArquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def adicionarArquivo(texto):
    arquivo = open('teste.txt','a')
    arquivo.write('\n')
    arquivo.write(texto)
    arquivo.close()


def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo)
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    # escreverArquivo('Primeira Escrita\n')
    # adicionarArquivo('Segunda Escrita\n')
    # adicionarArquivo('Quarta Escrita\n')
    lerArquivo('teste.txt')

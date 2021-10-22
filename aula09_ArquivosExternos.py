# 'w' -> Escreve em um arquivo OBS: Limpa o que já tem
# 'a' -> Adiciona ao arquivo existente
caminho = 'E:/Alladio/projetos/python/alunos.txt'
def escreverArquivo(texto, caminhoArquivo):
    diretorioArquivo = caminhoArquivo
    arquivo = open(diretorioArquivo,'w')
    arquivo.write(texto)
    arquivo.close()

def adicionarArquivo(texto,caminhoArquivo):
    arquivo = open(caminhoArquivo,'a')
    # arquivo.write('\n')
    arquivo.write(texto)
    arquivo.close()


def lerArquivo(caminhoArquivo):
    arquivo = open(caminhoArquivo)
    texto = arquivo.read()
    # print(texto)

def mediaNotas(caminhoArquivo):
    arquivo = open(caminhoArquivo)
    alunoNota = arquivo.read()
    # print(alunoNota)

    alunoNotaSplit = alunoNota.split('\n')
    # print(alunoNota)
    for x in alunoNota:
        alunoNotaSplit2 = x.split(',')
        # aluno =x[0]
        print(alunoNotaSplit2)

if __name__ == '__main__':
    caminhoArquivo=caminho
    # escreverArquivo('Primeira Escrita\n')
    # adicionarArquivo('Segunda Escrita\n')
    # adicionarArquivo('Quarta Escrita\n')
    # escreverArquivo('Alladio, 10,9,10,9\n',caminhoArquivo)
    # adicionarArquivo('Valentim, 9,9,9,9\n',caminhoArquivo)
    # adicionarArquivo('Octavio, 8,8,8,8\n',caminhoArquivo)
    # lerArquivo(caminhoArquivo)
    mediaNotas(caminhoArquivo)
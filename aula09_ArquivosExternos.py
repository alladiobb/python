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
    arquivo = open(caminhoArquivo,'r')
    alunoNota = arquivo.read()
    # print(alunoNota)
    alunoNotaSplitado = alunoNota.split('\n')
    # print(alunoNotaSplit)
    listaMedia=[]

    # Função Lambda para fazer a média das notas
    media = lambda notas: sum([int(i) for i in notas]) / 4

    for x in alunoNotaSplitado:

        listaNotas = x.split(',')
        aluno =listaNotas[0]
        listaNotas.pop(0)
        # print(aluno)
        # print(listaNotas)
        # print(media(listaNotas))
        listaMedia.append({aluno:media(listaNotas)})
    return listaMedia

#Copiar arquivo
def copiaArquivo(caminhoArquivoBase,caminhoCopia):
    import shutil
    shutil.copy(caminhoArquivoBase,caminhoCopia)

#Mover arquivo
def moveArquivo(caminhoArquivoBase,caminhoNovo):
    import shutil
    shutil.move(caminhoArquivoBase,caminhoNovo)

if __name__ == '__main__':
    caminhoArquivo=caminho

    # escreverArquivo('Alladio,10,9,10,9\n',caminhoArquivo)
    # adicionarArquivo('Valentim,9,9,9,9\n',caminhoArquivo)
    # adicionarArquivo('Octavio,8,8,8,8\n',caminhoArquivo)
    # lerArquivo(caminhoArquivo)

    # listaMedia=mediaNotas(caminhoArquivo)
    # print(listaMedia)

    # copiaArquivo(caminhoArquivo,'E:/')
    moveArquivo(caminhoArquivo,'E:/teste/')
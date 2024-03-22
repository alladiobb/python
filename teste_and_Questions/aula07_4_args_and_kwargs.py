def exibir_texto(data, *args, **kwargs):
    texto = "\n ".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_texto (
    "Brasil 22/03/2024",
    "Olá, bom dia, tudo bem?",
    "Esse é um texte de args...",
    "Masa vida é essa...",
    autor="Alladio",
    ano="2024")
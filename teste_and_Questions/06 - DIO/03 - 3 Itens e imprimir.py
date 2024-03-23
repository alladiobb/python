# Lista para armazenar os itens
itens = []
for i in range(3):
  item = input("Digite o item {}: ".format(i + 1))
  itens.append(item)
# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")
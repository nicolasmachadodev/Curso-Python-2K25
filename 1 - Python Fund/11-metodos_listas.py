gamesList = ["Red Dead Redemption 2", "Fifa 22", "GTA V", "Limbo", "Hollow Knight"]

# Adiciona um novo jogo ao final da lista
gamesList.append("Celeste")
print(gamesList)

# Insere um jogo na posição 2
gamesList.insert(2, "Minecraft")
print(gamesList)

# Remove um jogo pelo nome
gamesList.remove("Fifa 22")
print(gamesList)

# Remove o último jogo da lista
gamesList.pop()
print(gamesList)

# Encontra o índice de um jogo
index = gamesList.index("Limbo")
print("Índice de Limbo:", index)

# Conta quantas vezes um jogo aparece na lista
count = gamesList.count("GTA V")
print("GTA V aparece:", count, "vez(es)")

# Ordena a lista em ordem alfabética

print(f'Ordem: {sorted(gamesList, reverse=True)}')

# Inverte a ordem da lista
gamesList.reverse()
print(gamesList)

# Faz uma cópia da lista
gamesCopy = gamesList.copy()
print("Cópia da lista:", gamesCopy)

# Adiciona vários jogos de uma vez
gamesList.extend(["Portal 2", "The Witcher 3"])
print(gamesList)

# Remove todos os itens da lista
gamesList.clear()
print("Lista limpa:", gamesList)
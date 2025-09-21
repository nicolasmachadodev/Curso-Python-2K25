gamesTuple = ("Red Dead Redemption 2", "Fifa 22", "GTA V", "Limbo", "Hollow Knight")

print(gamesTuple)

# - Não é possível adicionar, remover ou modificar elementos em uma tupla
# - Tuplas são imutáveis

# 1 - Buscar os dois primeiros elementos da tupla
print(gamesTuple[:2])

# 2 - Encontrar o índice de um elemento
index = gamesTuple.index("GTA V")
print("Índice de GTA V:", index)

# 3 - Contar quantas vezes um elemento aparece na tupla
count = gamesTuple.count("Limbo")   
print("Limbo aparece:", count, "vez(es)")

# 4 - Verificar se um elemento está na tupla
is_in_tuple = "Fifa 22" in gamesTuple
print("Fifa 22 está na tupla?", is_in_tuple)

# 5 - Procurar um elemento especifico na tupla
ownedGame = gamesTuple.index("Hollow Knight")
ownedGame = gamesTuple[ownedGame]
print("Jogo encontrado:", ownedGame)
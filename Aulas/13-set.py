gamesSet = {"Red Dead Redemption 2", "Fifa 22", "GTA V", "Limbo", "Hollow Knight"}
print(gamesSet)

# Não é possível acessar elementos por índice, pois sets são não ordenados
# Os elementos são únicos, ou seja, não aceitam repetição
 
# 1 - Buscar o taamnho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {True, 1, 2, 3, 4, 5, }
print(exampleSet)

# 3 - Adicionar elementos de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item do set
gamesSet.remove("Limbo")
print(gamesSet)

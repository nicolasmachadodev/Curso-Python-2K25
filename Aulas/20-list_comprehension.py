# 1 - Liste valores de 0 a 10 que sejam menores do que 4.
# for i in range(10):
#     if i < 4:
#         print(i)

# List Comprehension

listNumbers = [print(i) for i in range(10) if i < 4]

gamesList = ["GTA V", "Assasins Creed", 'Minecraft', "Free Fire", "Need For Speed"]

# 2 - Recuperando jogos que possuem a letra "A"

gameWithA = [print(game) for game in gamesList if 'a' in game.lower()]

# 3 - Mostrando jogos que ja zerei

gamesFinished = [print(game) for game in gamesList if game != "Minecraft"]
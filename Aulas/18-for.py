gamesList = ["GTA V", "Minecraft", "FIFA 23", "The Last of Us"]

# 1 - Iterando valores de uma lista com for
for game in gamesList:
    print(game) 

# 2 - Quando a condicao for atendida o loop sera interrompido
for game in gamesList:
    if game == "FIFA 23":
        break
    print(game)

# 3 - Quando a condicao for atendida o loop pula para a proxima iteracao
for game in gamesList:
    if game == "FIFA 23":
        continue
    print(game)

# 4 - Avaliacao do jogo
gameName = input('Digite o nome do jogo: ')
gameRating = int(input('Quantas vezes deseja avaliar o jogo: '))

totalRating = 0
for i in range(gameRating):
    rating = float(input(f'Dê uma nota para o jogo {gameName} (0.0 a 10.0): '))
    totalRating += rating
print(f'A média das notas para o jogo {gameName} é {totalRating / gameRating:.1f}')
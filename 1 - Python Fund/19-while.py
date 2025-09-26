gameName = input('Digite o nome do jogo: > ')
rating = 0
qtdRatings = 0
totalRating = 0
averageRating = 0

while rating != -1:
    rating = float(input(f'Dê uma nota para o jogo {gameName}: '))
    if rating != -1:
        totalRating += rating
        qtdRatings += 1
averageRating = totalRating / qtdRatings
print(f'A média das notas para o jogo {gameName} é {averageRating:.1f}')

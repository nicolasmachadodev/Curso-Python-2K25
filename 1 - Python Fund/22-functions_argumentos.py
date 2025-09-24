# 1 - Crie uma função que receba dois nomes e imprima um nome completo.
def fullName(firstName, lastName):
    print(f"Nome completo: {firstName} {lastName}")

fullName('Nicolas', 'Eduardo')

# 2 - Crie uma função que receba dois números e retorne a soma entre eles.
def sum(a, b):
    return a + b

print(sum(5, 10))

# 3 - Argumentos default em funções
def address(country='Brasil'):
    print(f'Eu moro no {country}')

address()
address('Chile')

# 4 - Avaliação de um jogo
def gameAvaliation(qtdRating):
    gameName = input('Digite o nome do jogo: ')
    sum = 0
    for a in range(qtdRating):
        note = float(input('Digite uma nota: '))
        sum += note
    print(f"A media de avaliacao do jogo {gameName}, equivale a: {sum / qtdRating :.2f}")

rating = int(input('Quantas vezes deseja avaliar o jogo: '))
gameAvaliation(rating)
# 1 - Função para imprimir "Hello, World!"

def wellcome():
    print('Hello, World!')

wellcome()

# 2 - Função para somar dois números
def sum(a, b):
    return a + b

print(sum(5, 10))

# 3 - Função para cadastrar um jogo
def createGame():
    gameName = input("Nome do jogo: ")
    gameGenre = input("Gênero do jogo: ")
    yearLaunch = int(input("Ano de lançamento: "))
    noteRating = float(input("Nota do jogo (0 a 10): "))
    print(f"Jogo {gameName} cadastrado com sucesso!")

createGame()

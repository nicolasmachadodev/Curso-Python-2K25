"""
Exercício Final:
* Gerenciamento de Jogadores e Times
-> Escreva um programa em python que realize o gerenciamento de jogadores.
Ele deve atender aos seguintes requisitos:
1 - A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2 - A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3 - A opção de remover um time deve pedir um índice específico do time que foi cadastrado para fazer a sua exclusão.
4 - A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5 - A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que foi cadastrado no time.
6 - A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Obs: Este é o exercício de final do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.

"""


timesDict = {}
done = True

# Functions

def seeAll(timesDict):
    for index in timesDict:
        newDict = timesDict[index]
        for key in newDict.keys():
            print(f'{index} | {key} - Jogadores: {len(newDict[key]['Jogadores'])}')

def newPlayer():
    timeSelected = int(input('Qual time deseja adicionar um jogador?: '))
    newDict = timesDict[timeSelected]
    for key in newDict.keys():
        newPlayer = input('Digite o nome desse jogador: ')
        newDict[key]["Jogadores"].append(newPlayer)

def removePlayer():
    timeSelected = int(input('Qual time deseja remover um jogador?: '))
    newDict = timesDict[timeSelected]
    for key in newDict.keys():
        removePlayer = input('Digite o nome desse jogador: ')
        newDict[key]["Jogadores"].remove(removePlayer)

def seeAllPlayers():
    timeSelected = int(input('Qual time deseja listar: '))
    newDict = timesDict[timeSelected]
    for key in newDict.keys():
        count = 0
        for player in newDict[key]["Jogadores"]:
            count += 1
            print(f'{count} - {player}')
# Loop

while done:
    print("""
    Times de futebol.

1 - Adicionar um novo time
2 - Remover um time
3 - Listar todos os times
4 - Adicionar jogador
5 - Remover um jogador
6 - Listar jogadores de um time
7 - Sair""")
    
    option = int(input("Selecione: "))
    print('')
    if option == 1:
        newTime = input('Nome do time que deseja cadastrar: ')
        seuIndex = len(timesDict) + 1
        timesDict[seuIndex] = {newTime: {'Jogadores': []}}
    elif option == 2:
        removeTime = int(input("Digite o numero do time que deseja remover: "))
        del timesDict[removeTime]
        print('Time removido com sucesso!')
    elif option == 3:
        seeAll(timesDict)
    elif option == 4:
        newPlayer()
    elif option == 5:
        removePlayer()
    elif option == 6:
        seeAllPlayers()
    else:
        break;

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
def seeAll(timesDict):
    for key in timesDict:
        print(f"{key} - Jogadores: {len(timesDict[key]['Jogadores'])}")

while done:
    print("""Times de futebol.

1 - Adicionar um novo time
2 - Remover um time
3 - Listar todos os times
4 - Adicionar jogador
5 - Remover um jogador
6 - Listar jogadores de um time
7 - Sair""")
    


    option = int(input("Selecione: "))
    if option == 1:
        newTime = input('Nome do novo time: ')
        timesDict[newTime] = {"Jogadores": []}
    elif option == 3:
        seeAll(timesDict)
    elif option == 7:
        break;
    
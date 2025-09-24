import pprint

gamesDict = {
    'GTA V': {
        'classification': 9.6,
        'year': 2013,
        'genre': ['Acao', 'Aventura']
    },
    'Red Dead Redemption 2': {
        'classification': 9.8,
        'year': 2018,
        'genre': ['Acao', 'Aventura', 'Western']
    },
    'Minecraft': {
        'classification': 9.0,
        'year': 2011,
        'genre': ['Sandbox', 'Sobrevivencia', 'Aventura']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Acessar elementos dentro de um dicionario
print(gamesDict['GTA V']['year'])

# 2 - Adicionar novos elementos ao dicionario
gamesDict['Red Dead Redemption 2']['price'] = 179.90 # Adiciona um novo par chave/valor ao dicionario
pp.pprint(gamesDict)

# 3 - Remover elementos do dicionario
del gamesDict['Minecraft']['genre'][2] # Remove o terceiro elemento da lista na chave 'genre' do jogo 'Minecraft'
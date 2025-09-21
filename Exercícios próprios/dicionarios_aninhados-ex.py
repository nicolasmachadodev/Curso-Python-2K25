import pprint

# Exercícios sobre dicionários aninhados em Python

# 1. Crie um dicionário chamado filmesDict com pelo menos 2 filmes. 
#    Cada filme deve ser uma chave, e o valor deve ser outro dicionário com as chaves: 'nota', 'ano' e 'generos' (lista de gêneros).
#    Preencha com valores fictícios.

filmesDict = {
    'Fight Club': {
        'nota': 10,
        'ano': 1998,
        'generos': ['Luta', 'Acao']
    },
    'Interestelar': {
        'nota': 10,
        'ano': 2014,
        'generos': ['Ficcao Cientifica', 'Drama']
    }
}

# 2. Imprima o dicionário filmesDict de forma "bonita" usando pprint.

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDict)

# 3. Acesse e imprima o ano de lançamento do primeiro filme do seu dicionário.

print(filmesDict['Fight Club']['ano'])

# 4. Adicione uma nova chave chamada 'preco' ao segundo filme, com um valor fictício.

filmesDict['Interestelar']['preco'] = 99.90

# 5. Remova o primeiro gênero da lista de gêneros do primeiro filme.

del filmesDict['Fight Club']['generos'][0]

# 6. Imprima novamente o dicionário filmesDict para ver as alterações.

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDict)

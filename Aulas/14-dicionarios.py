gameFifa = {
    'name': 'FIFA 22',
    'year': 2021,
    'genre': ['Esporte', 'Familia'],
    'classification': 8.6,
    'price': 199.99
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Acessar elementos dentro de um dicionario
print(gameFifa["year"]) 
print(gameFifa.get("name")) # Forma mais segura, pois se a chave nao existir, nao da erro.

# 2 - Buscar apenas as chaves do dicionario
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionario
print(gameFifa.values())

# 4 - Buscar os itens do dicionario (chave e valor)
print(gameFifa.items())

# 5 - Adicionar novos elementos ao dicionario
gameFifa['players'] = 2 # Adiciona um novo par chave/valor ao dicionario
print(gameFifa)

# 6 - Atualizar elementos do dicionario
gameFifa.update({'players': 1}) # Atualiza o valor da chave 'players'
print(gameFifa)

# 7 - Remover elementos do dicionario
gameFifa.pop('classification') # Remove o par chave/valor da chave 'classification'
print(gameFifa)

del gameFifa['price']
print(gameFifa)

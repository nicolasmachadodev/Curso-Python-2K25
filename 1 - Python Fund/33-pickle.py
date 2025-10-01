import pickle

dados = {'name': 'Nicolas', 'idade': 16}

# 1 - Serializando sem salvar.
dadosSerializados = pickle.dumps(dados)
print(dadosSerializados)

# 2 - Desserializando os bytes
dadosRetorno = pickle.loads(dadosSerializados)
print(dadosRetorno)

# 3 - Serializando e salvando em arquivo.pkl
with open('dados.pkl', 'wb') as arq:
    pickle.dump(dados, arq)

# 4 - Desserializando um arquivo
with open('dados.pkl', 'rb') as arq:
    dadosDoFile = pickle.load(arq)
print(dadosDoFile)
arquivo = open("pessoas.txt", "r")


newList = list()
for dado in arquivo.readlines():
    newList.append(dado.split())

print(newList)

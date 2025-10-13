with open('pessoas.txt', 'w') as arq:
    arq.write("Testando\n")

with open('pessoas.txt', 'a') as arq:
    arq.write('testandoooooooooooooooo')

with open("pessoas.txt", "r") as arq:
    content = arq.read()
    print(content)
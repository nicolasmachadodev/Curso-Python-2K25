texto = "  Olá, mundo! Python é divertido.  "

# Remover espaços extras
print(texto.strip())       # "Olá, mundo! Python é divertido."
print(texto.lstrip())      # remove só da esquerda
print(texto.rstrip())      # remove só da direita

# Caixa alta / baixa
print(texto.upper())       # tudo MAIÚSCULO
print(texto.lower())       # tudo minúsculo
print(texto.capitalize())  # só a 1ª letra maiúscula
print(texto.title())       # 1ª letra de cada palavra maiúscula

# Substituir texto
print(texto.replace("divertido", "fácil"))  # troca palavras

# Encontrar posições
print(texto.find("Python"))   # índice onde começa "Python"
print(texto.find("Java"))     # -1 (não encontrou)

# Verificações
print(texto.startswith("  Olá"))  # True
print(texto.endswith("."))        # True
print("Python" in texto)          # True
print("Java" in texto)            # False

# Quebrar e juntar
lista = texto.split()       # quebra em lista de palavras
print(lista)

nova = "-".join(lista)      # junta com hífen
print(nova)

# Contar ocorrências
print(texto.count("o"))     # conta quantas vezes aparece "o"

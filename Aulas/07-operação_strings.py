# Declarando strings
nome = "Python"
fruta = 'banana'

# Tamanho da string
print(len(fruta))  # 6

# Acessando caracteres por índice
print(nome[0])     # P
print(nome[-1])    # n

# Concatenando
mensagem = "Olá, " + nome + "!"
print(mensagem)    # Olá, Python!

# Repetição
print("ha" * 3)    # hahaha

# Métodos comuns
print(fruta.upper())         # BANANA
print(fruta.capitalize())    # Banana
print(fruta.replace("na", "NA"))  # baNANA

# Verificando se contém algo
print("Py" in nome)          # True
print("Java" not in nome)    # True

# f-string (formatação moderna)
idade = 25
print(f"{nome} tem {idade} anos.")  # Python tem 25 anos.


# Exercícios de revisão completa Python (nível iniciante)
# Resolva os exercícios abaixo usando apenas o que foi ensinado nas aulas.

# 1. Crie uma variável chamada idade e atribua um valor inteiro a ela. Imprima o valor.
idade = 16
print(idade)

# 2. Peça ao usuário para digitar um número decimal e imprima o dobro desse número.
number = float(input("Digite um numero decimal: "))
print(f"Dobro: {number * 2}")

# 3. Crie uma string com seu nome completo e imprima apenas o primeiro nome.
fullName = "Nicolas Eduardo Machado dos Santos"
lista = fullName.split()
print(lista[0])

# 4. Crie duas variáveis, x e y, e imprima a soma, subtração, multiplicação e divisão inteira entre elas.
x = int(input("Primeiro numero: "))
y = int(input("Segundo numero: "))

print(f"Soma: {x + y}")
print(f"Subtração: {x - y}")
print(f"Multiplicação: {x * y}")
print(f"Divisão inteira: {x // y}")

# 5. Peça ao usuário para digitar uma frase e conte quantas vezes a letra 'a' aparece.

frase = input("Digite uma frase: ")
print(f"A letra 'A' aparece {frase.lower().count('a')} vezes")

# 6. Crie uma lista com 4 frutas. Imprima a segunda fruta.
fruits = ["Banana", "Pera", "Melancia", "Laranja"]
print(fruits[1])

# 7. Adicione uma fruta ao final da lista e imprima a lista.
fruits.append("Maçã")
print(fruits)

# 8. Remova a primeira fruta da lista e imprima a lista.
fruits.remove(fruits[0])
print(fruits)

# 9. Crie uma tupla com 3 números. Imprima o maior valor.
numberTuple = (4, 6 ,8)
maior = 0
for number in numberTuple:
    if number > maior:
        maior = number
print(maior)


# 10. Verifique se o número 5 está na tupla do exercício anterior.
for number in numberTuple:
    if number == 5:
        print("Numero 5 encontrado!")

# 11. Crie um set com 3 nomes de animais. Adicione um novo animal e remova um existente.
animalSet = {"Cachorro", "Gato", "Macaco"}
animalSet.pop()
animalSet.add("Golfinho")

# 12. Crie um dicionário chamado produto com as chaves 'nome', 'preco' e 'quantidade'. Imprima todas as chaves.
produto = {
    "nome": "Shampoo",
    "preco": 15.90,
    "quantidade": 85
}
print(produto.keys())

# 13. Atualize o valor da chave 'preco' do dicionário produto.
produto["preco"] = 12.90

# 14. Remova a chave 'quantidade' do dicionário produto.
del produto["quantidade"]
print(produto)

# 15. Crie um dicionário aninhado chamado escola, onde cada aluno tem um nome como chave e um dicionário com 'idade' e 'nota'.
escola = {
    'Nicolas': {
        'idade': 16,
        'nota': 10
    },
    'Emilly': {
        'idade': 16,
        'nota': 9.9
    }
}

# 16. Imprima a nota do segundo aluno do dicionário escola.
print(escola['Emilly']['nota'])

# 17. Peça ao usuário para digitar um texto e transforme tudo em minúsculo.
textUser = str(input("Digite um texto: "))
print(textUser.lower())

# 18. Crie uma lista de 5 números e imprima apenas os números pares.
listNumbers = [2, 5, 4, 3, 8]
for number in listNumbers:
    if number % 2 == 0:
        print(number)

# 19. Faça um slice da lista do exercício anterior para mostrar os 3 últimos elementos.
print(listNumbers[-3:])

# 20. Crie uma string e use o método .replace() para trocar uma letra por outra.
stringReplace = 'Nicolas'
stringReplace = stringReplace.replace("a", "4")
print(stringReplace)

# 21. Crie uma lista de nomes e use .join() para juntar todos os nomes separados por traço.
listNames = ['Nicolas', 'Emilly', 'Yuri']
names = '-'.join(listNames)
print(names)

# 22. Crie um dicionário com 2 filmes, cada um com 'ano' e 'genero'. Imprima todos os gêneros.
filmesDict = {
    'Interestelar': {
        'ano': 2014,
        'genero': 'Ficção Científica'
    },
    'Fight Club': {
        'ano': 1998,
        'genero': 'Luta'
    }
}
for key in filmesDict:
    print(filmesDict[key]['genero'])

# 23. Peça ao usuário para digitar um número e verifique se ele está na lista do exercício 18.
numberDigited = int(input('Digite um numero: '))
if numberDigited in listNumbers:
    print("O numero esta na lista do ex18.")
else:
    print('Nao encontrado.')

# 24. Crie uma tupla com 4 cores e imprima as duas últimas cores.
colorTuple = ('red', 'yellow', 'brown', 'green')
print(colorTuple[-2:])

# 25. Crie um set com 5 números e imprima o tamanho do set.
setNumbers = {3, 7, 13, 3, 8}
print(f"Tamanho do set: {len(setNumbers)}")

# 26. Crie uma lista de strings e ordene em ordem alfabética.
listString = ["ola", "Nicolas", "Teste", "Amor"]
listString.sort()
print(listString)

# 27. Crie um dicionário chamado carro com as chaves 'marca', 'modelo' e 'ano'. Imprima o valor de cada chave.
carro = {
    'marca': 'Porsche',
    'modelo': 'Cayenne',
    'ano': 2014
}
print(carro.values())

# 28. Atualize o valor da chave 'ano' do dicionário carro para o ano atual.
carro['ano'] = 2025 

# 29. Crie um dicionário aninhado chamado loja, onde cada produto tem um nome como chave e um dicionário com 'preco' e 'estoque'.
loja = {
    'shampoo': {
        'preco': 12.90,
        'estoque': 43
    },
    'condicionador': {
        'preco': 13.90,
        'estoque': 59
    }
}

# 30. Imprima o estoque do primeiro produto do dicionário loja.
print(loja['shampoo']['estoque'])

# 31. Peça ao usuário para digitar dois números e imprima qual é o maior.
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n1 == n2:
    print('Ambos são iguais.')
else:
    print(f'{n2} é maior que {n1}.')

# 32. Crie uma lista de 6 números e imprima a soma de todos os valores.
numbersList = [2, 5, 6, 3, 7, 23]
sum = 0
for i in numbersList:
    sum += i
print(sum)

# 33. Crie um dicionário chamado pessoa com as chaves 'nome', 'idade' e 'cidade'. Imprima uma frase usando os valores desse dicionário.
pessoa = {
    'nome': 'Nicolas',
    'cidade': 'Foz do Jordão',
    'idade': 16
}
print(f"Meu nome é {pessoa['nome']}, tenho {pessoa['idade']} anos e moro em {pessoa['cidade']}.")

# 34. Crie uma tupla com 5 letras e verifique se a letra 'a' está presente.
letterTuple = ('a', 'f', 's', 'y', 'q')
if 'a' in letterTuple:
    print('Letra "A" encontrada.')

# 35. Crie um set com 4 nomes e imprima todos os nomes em letras maiúsculas.
nameSet = {'Nicolas', 'Emilly', 'Yuri', 'Cristiane'}
for name in nameSet:
    print(name.upper())

# Super Desafio Python: Sistema de Academia Avançado

"""
Desafio: Crie um programa completo que:

1. Mostre um menu com opções para o usuário:
   - 1: Cadastrar aluno (nome, idade e plano)
   - 2: Remover aluno
   - 3: Listar todos os alunos cadastrados
   - 4: Pesquisar aluno pelo nome
   - 5: Mostrar apenas alunos maiores de idade
   - 6: Transformar todos os nomes em maiúsculo
   - 7: Trocar o plano atual de um aluno
   - 8: Sair do sistema

2. Armazene os alunos em uma lista de dicionários, onde cada dicionário contém:
   - nome (str)
   - idade (int)
   - plano (str: "mensal", "trimestral" ou "anual")

3. Para a opção de pesquisa (4):
   - Mostre todos os alunos cujo nome contenha a palavra digitada (ignorar maiúsculas/minúsculas).

4. Para a opção de maiores de idade (5):
   - Mostre apenas os alunos com idade >= 18.

5. Para a opção de transformar nomes (6):
   - Atualize todos os nomes para maiúsculo.

6. Para a opção de calcular valores (7):
   - Crie uma listagem de todos os alunos com o respectivo valor a pagar segundo o plano escolhido.

Regras:
- Use apenas recursos já vistos nas aulas.
- Use listas, dicionários, laços, input, print, if/else, while, map, filter, etc.
- Não use bibliotecas externas.
- O sistema deve rodar até que o usuário escolha a opção "Sair".
"""
def addNew(name, idade, plano, listDict):
   if plano == "1":
      listDict.append({'name': name.capitalize(), 'idade': idade, 'plano': 'Semanal'})
   elif plano == "2":
      listDict.append({'name': name.capitalize(), 'idade': idade, 'plano': 'Mensal'})
   elif plano == "3":
      listDict.append({'name': name.capitalize(), 'idade': idade, 'plano': 'Anual'}) 
   else:
      print('Plano invalido.')

def removeOne(nameRemove, listDict):
   for index, dic in enumerate(listDict):
      if dic['name'] == nameRemove.capitalize():
         listDict.remove(listDict[index])

def seeAll(listDict):
   for index, dic in enumerate(listDict):
      print(f'Nome: {dic['name']}\nIdade: {dic['idade']}\nPlano: {dic['plano']}')

listDict = list()
while True:
   print("""\n-_-_-_-_-_-_-_Academy System_-_-_-_-_-_-_-
         
1 - Cadastrar aluno
2 - Remover aluno
3 - Listar todos os alunos
4 - Listar alunos pelo nome
5 - Mostrar apenas alunos maiores de idade
6 - Transformar todos os nomes em maiusculo
7 - Alterar o plano mensal de algum aluno
8 - Sair do programa""")
   choice = input('> ')
   
   print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
   if choice == '1':
      name = input("Digite o nome do aluno:\n> ")
      idade = int(input('Digite a idade do aluno:\n> '))
      plano = input('Qual plano o anulo adquiriu?\n1 - Semanal\n2 - Mensal\n3 - Anual\n> ')
      addNew(name, idade, plano, listDict)
         
         
   elif choice == '2':
      nameRemove = input('Digite o nome do aluno que deseja remover:\n> ')
      removeOne(nameRemove, listDict)
         
                
   elif choice == '3':
      seeAll(listDict)


   elif choice == '4':
      pass
   elif choice == '5':
      pass
   elif choice == '6':
      pass
   elif choice == '7':
      pass
   elif choice == '8':
      pass

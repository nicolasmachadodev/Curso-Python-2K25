# Super Desafio Python: Sistema de Academia Avançado

"""
Desafio: Crie um programa completo que:

1. Mostre um menu com opções para o usuário:
   - 1: Cadastrar aluno (nome, idade e plano)
   - 2: Remover aluno
   - 3: Listar todos os alunos cadastrados
   - 4: Pesquisar aluno pelo nome
   - 5: Mostrar apenas alunos maiores de idade
   - 6: Trocar o plano atual de um aluno
   - 7: Salvar relatorio dos alunos atuais em um arquivo
   - 8: Recuperar todos os alunos salvos
   - 9: Sair do sistema

2. Armazene os alunos em uma lista de dicionários, onde cada dicionário contém:
   - nome (str)
   - idade (int)
   - plano (str: "mensal", "trimestral" ou "anual")

3. Para a opção de pesquisa (4):
   - Mostre todos os alunos cujo nome contenha a palavra digitada (ignorar maiúsculas/minúsculas).

4. Para a opção de maiores de idade (5):
   - Mostre apenas os alunos com idade >= 18.

6. Para a opção de calcular valores (7):
   - Crie uma listagem de todos os alunos com o respectivo valor a pagar segundo o plano escolhido.

Regras:
- Use apenas recursos já vistos nas aulas.
- Use listas, dicionários, laços, input, print, if/else, while, etc.
- Não use bibliotecas externas.
- O sistema deve rodar até que o usuário escolha a opção "Sair".
"""

from time import sleep; import pickle

def addNew(name, idade, plano, listDict):
   if plano == "1":
      listDict.append({'name': name.capitalize(), 'idade': idade, 'plano': 'Trimestral'})
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
      print(f"Nome: {dic['name']}\nIdade: {dic['idade']}\nPlano: {dic['plano']}\n")

def seeByName(name, listDict):
   for index, dic in enumerate(listDict):
      if dic['name'] in name.capitalize():
         print(f"\nNome: {dic['name']}\nIdade: {dic['idade']}\nPlano: {dic['plano']}\n")

def onlyOver18(listDict):
   for index, dic in enumerate(listDict):
      if dic['idade'] >= 18:
         print(f"\nNome: {dic['name']}\nIdade: {dic['idade']}\nPlano: {dic['plano']}\n")

def changePlan(name, newPlan, listDict):
   for index, dic in enumerate(listDict):
      if dic['name'] == name.capitalize():
         if newPlan == '1':
            dic['plano'] = 'Trimestral'
         elif newPlan == '2':
            dic['plano'] = 'Mensal'
         elif newPlan == '3':
            dic['plano'] = 'Anual'
         else:
            print('Valor inexistente.')

def saveAll(listDict):
   with open('members.pkl', 'wb') as arq:
      pickle.dump(listDict, arq)
   print('Salvo com sucesso!')
def returnDados():
   try:
      with open('members.pkl', 'rb') as arq:
         listDict = pickle.load(arq)
         return listDict
   except:
      with open('members.pkl', 'wb') as arq:
         listVazia = []
         pickle.dump(listVazia, arq)

def deleteAll():
     with open('members.pkl', 'wb') as arq:
        pickle.dump([], arq)

returnDados()
listDict = returnDados()

while True:
   sleep(1)
   print("""\n-_-_-_-_-_-_-_-_-_Gym System_-_-_-_-_-_-_-_-_-
         
1 - Cadastrar aluno
2 - Remover aluno
3 - Listar todos os alunos
4 - Listar alunos pelo nome
5 - Mostrar apenas alunos maiores de idade
6 - Alterar o plano de algum aluno
7 - Salvar todos os alunos
8 - Excluir todos os alunos
9 - Sair do programa""")
   choice = input('> ')
   
   print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
   if choice == '1':
      name = input("Digite o nome do aluno:\n> ")
      idade = int(input('Digite a idade do aluno:\n> '))
      plano = input('Qual plano o anulo adquiriu?\n1 - Trimestral\n2 - Mensal\n3 - Anual\n> ')
      addNew(name, idade, plano, listDict)
         
         
   elif choice == '2':
      nameRemove = input('Digite o nome do aluno que deseja remover:\n> ')
      removeOne(nameRemove, listDict)
         
                
   elif choice == '3':
      seeAll(listDict)


   elif choice == '4':
      name = input('Digite o nome do aluno:\n> ')
      seeByName(name, listDict)


   elif choice == '5':
      onlyOver18(listDict)


   elif choice == '6':
      nome = input('Digite o nome do aluno:\n> ')
      planChange = input("""Planos:
                         
1 - Trimestral
2 - Mensal
3 - Anual

> """)
      changePlan(nome, planChange, listDict)


   elif choice == '7':
      saveAll(listDict)

   elif choice == '8':
      listDict.clear()
      deleteAll()

   elif choice == '9':
      print('Finalizando...')
      sleep(3)
      break

   else:
      print("Opção inválida.")

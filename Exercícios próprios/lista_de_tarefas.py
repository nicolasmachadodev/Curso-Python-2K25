"""
🧠 Desafio Python: Controle de Tarefas Inteligente

🎯 Objetivo:
Criar um sistema simples de gerenciamento de tarefas no terminal.

📝 Regras:
1. Mostrar um menu com as opções:
   1️⃣ Adicionar tarefa
   2️⃣ Listar tarefas
   3️⃣ Marcar tarefa como concluída
   4️⃣ Remover tarefa
   5️⃣ Sair

2. Armazenar as tarefas em uma lista de dicionários, onde cada tarefa contém:
   {"nome": "Estudar Python", "concluida": False}

3. Ao marcar como concluída, mudar o valor "concluida" para True.

4. Ao listar, mostrar as tarefas assim:
   [ ] 1 - Estudar Python
   [x] 2 - Fazer exercício de listas

5. O programa só termina quando o usuário escolher “5”.

💡 Desafio extra:
Salve e carregue as tarefas automaticamente de um arquivo tarefas.pkl usando o módulo pickle.
"""

from time import sleep; import pickle

def addNew(listDict):
   nameTask = input('Qual sera a tarefa: ')
   listDict.append({'nome': nameTask, 'concluido': False})
   print('Tarefa adicionada.')

def seeAll(listDict):
   for index, dic in enumerate(listDict, 1):
      status = "[X]" if dic['concluido'] else "[ ]"
      print(f"{status} {index} - {dic['nome']}")

def savePkl(listDict):
   with open('tasks.pkl', 'wb') as arq:
      pickle.dump(listDict, arq)

def loadFile():
   try:
      with open('tasks.pkl', 'rb') as arq:
         listDict = pickle.load(arq)
         return listDict
   except:
      with open('tasks.pkl', 'wb') as arq:
         listVazia = []
         pickle.dump(listVazia, arq)
         return listVazia

def removeTask(listDict):
   try:
      nameTask = int(input('Digite o numero da tarefa que deseja remover.\n> '))
      listDict.remove(listDict[nameTask - 1])
   except:
      print('Erro, tente uma opção válida.')

def task_concluida(listDict):
   try:
      nameTask = int(input('Digite o numero da tarefa.\n> '))
      listDict[nameTask - 1]['concluido'] = True
   except:
      print('Erro, tente uma opção válida.')


      

listDict = loadFile()

while True:
   sleep(1)
   print("""
   Gerenciador de tarefas.
          
1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Marcar tarefa como concluída
4 - Remover Tarefa
5 - Sair\n""")

   choice = input('> ')
   print('')

   if choice == "1":
      addNew(listDict)
      savePkl(listDict)
   
   elif choice == "2":
      seeAll(listDict)
      

   elif choice == "3":
      task_concluida(listDict)
      savePkl(listDict)

   elif choice == "4":
      removeTask(listDict)
      savePkl(listDict)

   elif choice == "5":
      print('Finalizando...')
      break

   else:
      print('Invalido.')
   

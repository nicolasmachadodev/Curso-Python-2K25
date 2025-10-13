"""
🏋️‍♂️ MEGA DESAFIO PYTHON: Sistema de Academia Ultimate

🎯 Objetivo:
Criar um sistema COMPLETO de gerenciamento de alunos e treinos da academia.

---------------------------------------------------

💪 FUNCIONALIDADES OBRIGATÓRIAS:

1️⃣ Cadastrar aluno  
   - Pedir nome, idade, plano (Mensal, Trimestral, Anual), peso e altura  
   - Calcular o IMC automaticamente  
   - Guardar os dados num dicionário  
   - Salvar tudo em “alunos.pkl” (com pickle)

2️⃣ Listar todos os alunos  
   - Mostrar nome, idade, plano e IMC formatado com 2 casas decimais  
   - Exibir quantos alunos estão cadastrados

3️⃣ Pesquisar aluno  
   - Buscar pelo nome  
   - Exibir todos os dados do aluno (inclusive IMC)

4️⃣ Atualizar dados  
   - Permitir mudar peso, altura ou plano  
   - Recalcular IMC automaticamente  
   - Atualizar o arquivo

5️⃣ Excluir aluno  
   - Remover completamente do sistema e do arquivo

6️⃣ Adicionar treinos a um aluno  
   - Cada aluno pode ter uma lista de treinos  
   - Exemplo: ["Peito e Tríceps", "Perna", "Costas e Bíceps"]  
   - Permitir adicionar e remover treinos

7️⃣ Ranking de IMC  
   - Mostrar os 3 alunos com melhor IMC (menor IMC → mais saudável)  
   - Usar `sorted()` com lambda e list comprehension

8️⃣ Backup automático  
   - Ao sair do programa, salvar os dados em “backup.pkl”

9️⃣ Log de ações  
   - Criar um arquivo “log.txt”  
   - Cada ação (cadastrar, editar, excluir) deve registrar data e hora

---------------------------------------------------

💾 BONUS (opcional):

- Adicione cores no terminal (ANSI codes):
  - Verde para sucesso
  - Vermelho para erro
  - Amarelo para avisos

- Mostre sempre o horário atual no topo do menu principal.

---------------------------------------------------

⚙️ DICA DE ESTRUTURA DO CÓDIGO:

1️⃣ Funções principais:
   - `carregar_dados()`
   - `salvar_dados()`
   - `cadastrar_aluno()`
   - `listar_alunos()`
   - `buscar_aluno()`
   - `atualizar_aluno()`
   - `excluir_aluno()`
   - `gerenciar_treinos()`
   - `ranking_imc()`
   - `registrar_log()`

2️⃣ Loop principal:
   - Menu com opções numeradas (1 a 9)
   - Try/except para evitar erros de input

3️⃣ Estrutura do dicionário:
   aluno = {
       "nome": "João",
       "idade": 20,
       "plano": "Mensal",
       "peso": 70.0,
       "altura": 1.75,
       "imc": 22.86,
       "treinos": ["Peito e Tríceps", "Perna"]
   }
"""

# 💡 Dica extra: use round(valor, 2) para formatar o IMC.

from time import sleep
from datetime import datetime
import pickle




#    8888888888                         888    d8b                            
#    888                                888    Y8P                            
#    888                                888                                   
#    8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b  
#    888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K      
#    888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b. 
#    888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88 
#    888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P' 

def new_log(text):
   formato = "[%d/%m/%Y] %H:%M:%S - "
   data = datetime.now()
   dataAtual = data.strftime(formato)
   with open('logs.txt', 'a') as arq:
      arq.write(f"{dataAtual}{text}\n")

def novo_aluno(listAlunos):
   # Obtendo dados do aluno.
   try:
      nameAluno = input('Digite o nome do aluno.\n> ')
      idadeAluno = int(input('Digite a idade do aluno.\n> '))
      planoAluno = int(input("""Qual o plano do aluno?\n\n1 - Mensal\n2 - Trimestral\n3 - Anual\n> """))
      pesoAluno = float(input('Qual o peso do aluno? Ex: 75.30\n> '))
      alturaAluno = float(input('Qual a altura do aluno? Ex: 1.83\n> '))
   except:
      print('Insira valores válidos.')

   # Criando um dict para cada aluno.
   novoAluno = {
      'nome': nameAluno.capitalize(),
      'idade': idadeAluno,
      'plano': 'indefinido',
      'peso': pesoAluno,
      'altura': alturaAluno,
      'imc': round(pesoAluno / (alturaAluno ** 2), 2)
               }
   if planoAluno == 1:
      novoAluno['plano'] = 'Mensal'
   elif planoAluno == 2:
      novoAluno['plano'] = 'Trimestral'
   elif planoAluno == 3:
      novoAluno['plano'] = 'Anual'
   else:
      print('\nPlano inválido.')
      return

   # Adicionando novo aluno na lista de alunos.
   novoAluno['treinos'] = []
   listAlunos.append(novoAluno)
   new_log(f'Usúario adicionou um novo aluno chamado: {nameAluno}')
   print('\nAluno Adicionado com sucesso.')



def listar_alunos(listAlunos):
   if len(listAlunos) > 0:
      print(f"Total de alunos cadastrados: {len(listAlunos)}\n")
      print(f"{'Nome':<15} | {'Plano':<12} | {'Idade':<5} | {'IMC':<6}")
      print("-" * 50)
      for aluno in listAlunos:
         print(f"{aluno['nome']:<15} | {aluno['plano']:<12} | {aluno['idade']:<5} | {aluno['imc']:<6}")
      new_log(f'Usúario listou todos os alunos.')
   else:
      print('Nenhum aluno cadastrado.')



def pesquisar_aluno(listAlunos):
   nameAluno = input('Digite o nome dos alunos que deseja encontrar.\n> ')
   verify = False
   for aluno in listAlunos:
      if nameAluno.lower() in aluno['nome'].lower():
         verify = True
         print(f"""
     {aluno['nome']}
Idade: {aluno['idade']} anos
Altura: {aluno['altura']:.2f}
Peso: {aluno['peso']}
Plano: {aluno['plano']}
IMC: {aluno['imc']}\n""")
      new_log(f'Usúario pesquisou sobre os alunos(as) chamados: {nameAluno.capitalize()}')
   if not verify:
      print(f'Nenhum resultado encontrado para o nome: {nameAluno}')
      


def atualizar_dados(listAlunos):
   nameAluno = input('Digite o nome do aluno que deseja fazer alterações.\n> ')
   for aluno in listAlunos:
      if nameAluno.lower() in aluno['nome'].lower():
         choiceChange = input(f"""
         Selecione a alteração que deseja fazer:
Aluno(a): {aluno['nome']}

1 - Idade
2 - Peso
3 - Altura
4 - Plano
5 - Proximo/Sair
                              
> """)
         try:
            if choiceChange == '1':
               newIdade = int(input('Digite a nova idade.\n> '))
               new_log(f'Usúario mudou a idade do aluno(a): {aluno['nome']} | Antes: {aluno['idade']} anos - Depois: {newIdade} anos.')
               aluno['idade'] = newIdade
               print('\nIdade alterada.')
            elif choiceChange == '2':
               newPeso = float(input('Digite o novo peso.\n> '))
               new_log(f'Usúario mudou o peso do aluno(a): {aluno['nome']} | Antes: {aluno['peso']}KG. - Depois: {newPeso}KG.')
               aluno['peso'] = newPeso; aluno['imc'] = round(newPeso / (aluno['altura'] ** 2), 2)
               print('\nPeso alterado.')
            elif choiceChange == '3':
               newAltura = float(input('Digite a nova altura.\n> '))
               new_log(f'Usúario mudou a altura do aluno(a): {aluno['nome']} | Antes: {aluno['altura']} - Depois: {newAltura}')
               aluno['altura'] = round(newAltura, 2); aluno['imc'] = round(aluno['peso'] / (newAltura ** 2), 2)
               print('\nAltura alterada.')
            elif choiceChange == '4':
               newPlano = int(input("""Qual o novo plano do aluno?\n\n1 - Mensal\n2 - Trimestral\n3 - Anual\n> """))
               if newPlano == 1:
                  new_log(f'Usúario alterou o plano do aluno(a): {aluno['nome']} | Antes: Plano {aluno['plano']} - Depois: Plano Mensal')
                  aluno['plano'] = 'Mensal'
                  print('\nPlano alterado com sucesso!')
                  
               elif newPlano == 2:
                  new_log(f'Usúario alterou o plano do aluno(a): {aluno['nome']} | Antes: Plano {aluno['plano']} - Depois: Plano Trimestral')
                  aluno['plano'] = 'Trimestral'
                  print('\nPlano alterado com sucesso!')
                  
               elif newPlano == 3:
                  new_log(f'Usúario alterou o plano do aluno(a): {aluno['nome']} | Antes: Plano {aluno['plano']} - Depois: Plano Anual')
                  aluno['plano'] = 'Anual'
                  print('\nPlano alterado com sucesso!')
                  
               else:
                  print('Valor inválido.')
                  return
            elif choiceChange == '5':
               continue
            else:
               print('Opção inválida.')
               return
         except:
            print('\nInsira um valor correto.')
            return



def excluir_aluno(listAlunos):
   nameAluno = input('Digite o nome do aluno que deseja remover.\n> ')
   for aluno in listAlunos:
      if nameAluno.lower() in aluno['nome'].lower():
         removeChoice = input(f"""\nAluno Selecionado: {aluno['nome']}

1 - Remover
2 - Não remover
               
> """)
         if removeChoice == '1':
            new_log(f'Usúario removeu o aluno: {aluno['nome']}')
            listAlunos.remove(aluno)
            print('\nAluno removido com sucesso.')
         elif removeChoice == '2':
            continue
         else:
            print('Opção inválida.')
            


def gerenciar_treinos(listAlunos):
   choice = input(f"""Selecione a opção:

1 - Adicionar treinos
2 - Remover Treinos
3 - Listar treinos   
               
> """)
   if choice == '1':
      nameAluno = input('Digite o nome do aluno que deseja adicionar treinos.\n> ')
      for aluno in listAlunos:
         if nameAluno.lower() in aluno['nome'].lower():
            choice = input(f'\nAluno selecionado: {aluno['nome']}\n\n1 - Adicionar\n2 - Proximo/Sair\n> ')
            if choice == '1':
               treino = input("Qual seria o treino que deseja adicionar?\n> ")
               new_log(f'Usúario adicionou um novo treino ao aluno: {aluno['nome']} | Treino: {treino}')
               aluno['treinos'].append(treino)
            else:
               print('Voltando ao menu inicial.')

   elif choice == '2':
      nameAluno = input('Digite o nome do aluno que deseja remover treinos.\n> ')
      for aluno in listAlunos:
         if nameAluno.lower() in aluno['nome'].lower():
            choice = input(f'\nAluno selecionado: {aluno['nome']}\n\n1 - Remover\n2 - Proximo/Sair\n> ')
            if choice == '1':
               try:
                  indexTreino = int(input('Digite o número exato do treino que deseja remover. Liste todos primeiro! \n0 - Sair\n> '))
                  if indexTreino != 0:
                     new_log(f'Usúario removeu um treino do aluno: {aluno['nome']} | Treino: {aluno['treinos'][indexTreino - 1]}')
                     aluno['treinos'].remove(aluno['treinos'][indexTreino - 1])
                     print('Treino removido com sucesso!')
                  else:
                     print('Saindo.')
                     break
               except:
                  print('Digite um valor válido.')

   elif choice == '3':
      nameAluno = input('Digite o nome do aluno que deseja listar treinos.\n> ')
      for aluno in listAlunos:
         if nameAluno.lower() in aluno['nome'].lower():
            if len(aluno['treinos']) > 0:
               new_log(f'Usúario listou os treinos dos alunos chamados(as): {nameAluno.capitalize()}')
               print(f"""
        {aluno['nome']}
                  
Treinos:""")
               for i, treino in enumerate(aluno['treinos']):
                  print(f"{i + 1} - {treino}")
            else:
               continue



def ranking_imc(listAlunos):
   
   listIMC = [aluno['imc'] for aluno in listAlunos]
   listIMC.sort()
   c = 0
   if len(listAlunos) >= 3:
      print(f'{"POSIÇÃO":<7} | {"NOME":<17} | {"IMC":<6}')
      print('-' * 40)
      for imc in listIMC[:3]:
         for aluno in listAlunos:
            if imc == aluno['imc']:
               c += 1
               print(f'{c:^7} | {aluno['nome']:<17} | {aluno['imc']:<6}')
      print('-' * 40)
      new_log(f'Usúario analisou o rankings de melhores IMCs')
   else:
      print('\nÉ necessário no mínimo 3 alunos para obter o ranking de IMC.')



def backup(listAlunos):
   listAlunosMod = listAlunos
   choice = input('Selecione:\n1 - Criar novo backup\n2 - Carregar backup anterior\n3 - Sair\n> ')
   if choice == '1':
      with open('backup.pkl', 'wb') as arq:
         pickle.dump(listAlunos, arq)
      new_log(f'Usúario criou um novo backup')
      print('Backup feito com sucesso.')
   elif choice == '2':
      try:
         with open('backup.pkl', 'rb') as arq:
            listAlunosMod = pickle.load(arq)
         new_log(f'Usúario carregou um backup antigo.')
         print('Backup carregado com sucesso.')
      except:
         print('Erro. Tente criar um novo backup!')
         return listAlunosMod
   elif choice == '3':
      print('Retornando...')
   return listAlunosMod



def logs():
   choice = input('Selecione:\n1 - Mostrar logs\n2 - Apagar logs\n3 - Sair\n> ')
   if choice == '1':
      with open('logs.txt', 'r') as arq:
         file = arq.read()
      if file == '':
         print("Logs vazias. Nada a ser mostrado!")
      else:
         print(file)
   elif choice == '2':
      with open('logs.txt', 'w') as arq:
         arq.write('')
      print('Logs apagadas.')
   elif choice == '3':
      print('Voltando ao menu.')
   else:
      print('Digite uma opção válida. Voltando ao menu.')


def init_logs():
   try:
      with open('logs.txt', 'r') as arq:
         arq.write("")
   except:
      with open('logs.txt', 'w') as arq:
         arq.write("")
               

#    888b     d888                            
#    8888b   d8888                            
#    88888b.d88888                            
#    888Y88888P888  .d88b.  88888b.  888  888 
#    888 Y888P 888 d8P  Y8b 888 "88b 888  888 
#    888  Y8P  888 88888888 888  888 888  888 
#    888   "   888 Y8b.     888  888 Y88b 888 
#    888       888  "Y8888  888  888  "Y88888                         


# Inicializando logs.
init_logs()
listAlunos = list()
while True:
   sleep(3)
   print(r"""
  /$$$$$$                                 /$$$$$$                        /$$                            
 /$$__  $$                               /$$__  $$                      | $$                            
| $$  \__/ /$$   /$$ /$$$$$$/$$$$       | $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$ 
| $$ /$$$$| $$  | $$| $$_  $$_  $$      |  $$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$
| $$|_  $$| $$  | $$| $$ \ $$ \ $$       \____  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$ \ $$ \ $$
| $$  \ $$| $$  | $$| $$ | $$ | $$       /$$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$ | $$ | $$
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$ | $$ | $$
 \______/  \____  $$|__/ |__/ |__/       \______/  \____  $$|_______/    \___/   \_______/|__/ |__/ |__/
           /$$  | $$                               /$$  | $$                                            
          |  $$$$$$/                              |  $$$$$$/                                            
           \______/                                \______/                                             
          
1 - Cadastrar aluno
2 - Listar todos os alunos
3 - Pesquisar aluno
4 - Atualizar dados
5 - Excluir aluno
6 - Adicionar/Remover treinos de um aluno
7 - Ranking de IMC
8 - Backup automático
9 - Log de ações
10 - Sair

--------------------------------------""")
   choice = input('\n> ')

#       ___          _           _                          _                   
#      / __\__ _  __| | __ _ ___| |_ _ __ __ _ _ __    __ _| |_   _ _ __   ___  
#     / /  / _` |/ _` |/ _` / __| __| '__/ _` | '__|  / _` | | | | | '_ \ / _ \ 
#    / /__| (_| | (_| | (_| \__ \ |_| | | (_| | |    | (_| | | |_| | | | | (_) |
#    \____/\__,_|\__,_|\__,_|___/\__|_|  \__,_|_|     \__,_|_|\__,_|_| |_|\___/ 
#                                                                               
   if choice == "1":
      try:
         novo_aluno(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar adicionar um novo aluno. Tente novamente! Erro: {e}')


#       __ _     _                     _                       
#      / /(_)___| |_ __ _ _ __    __ _| |_   _ _ __   ___  ___ 
#     / / | / __| __/ _` | '__|  / _` | | | | | '_ \ / _ \/ __|
#    / /__| \__ \ || (_| | |    | (_| | | |_| | | | | (_) \__ \
#    \____/_|___/\__\__,_|_|     \__,_|_|\__,_|_| |_|\___/|___/
#                                                              
   elif choice == "2":
      try:
         listar_alunos(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar listar os alunos. Tente novamente! Erro: {e}')
      


#       ___                      _                        _                   
#      / _ \___  ___  __ _ _   _(_)___  __ _ _ __    __ _| |_   _ _ __   ___  
#     / /_)/ _ \/ __|/ _` | | | | / __|/ _` | '__|  / _` | | | | | '_ \ / _ \ 
#    / ___/  __/\__ \ (_| | |_| | \__ \ (_| | |    | (_| | | |_| | | | | (_) |
#    \/    \___||___/\__, |\__,_|_|___/\__,_|_|     \__,_|_|\__,_|_| |_|\___/ 
#                       |_|                                                   
   elif choice == "3":
      try:
         pesquisar_aluno(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar pesquisar um aluno. Tente novamente! Erro: {e}')
      


#       _   _               _ _                     _           _           
#      /_\ | |_ _   _  __ _| (_)______ _ _ __    __| | __ _  __| | ___  ___ 
#     //_\\| __| | | |/ _` | | |_  / _` | '__|  / _` |/ _` |/ _` |/ _ \/ __|
#    /  _  \ |_| |_| | (_| | | |/ / (_| | |    | (_| | (_| | (_| | (_) \__ \
#    \_/ \_/\__|\__,_|\__,_|_|_/___\__,_|_|     \__,_|\__,_|\__,_|\___/|___/
#                                                                           
   elif choice == "4":
      try:
         atualizar_dados(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar atualizar os dados. Tente novamente! Erro: {e}')

#       __          _       _              _                   
#      /__\_  _____| |_   _(_)_ __    __ _| |_   _ _ __   ___  
#     /_\ \ \/ / __| | | | | | '__|  / _` | | | | | '_ \ / _ \ 
#    //__  >  < (__| | |_| | | |    | (_| | | |_| | | | | (_) |
#    \__/ /_/\_\___|_|\__,_|_|_|     \__,_|_|\__,_|_| |_|\___/ 
#                                                              
   elif choice == "5":
      try:
         excluir_aluno(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar excluir o aluno. Tente novamente! Erro: {e}')

#       _       _     _   _            _                 
#      /_\   __| | __| | | |_ _ __ ___(_)_ __   ___  ___ 
#     //_\\ / _` |/ _` | | __| '__/ _ \ | '_ \ / _ \/ __|
#    /  _  \ (_| | (_| | | |_| | |  __/ | | | | (_) \__ \
#    \_/ \_/\__,_|\__,_|  \__|_|  \___|_|_| |_|\___/|___/
#                                                        
   elif choice == "6":
      try:
         gerenciar_treinos(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar gerenciar os treinos. Tente novamente! Erro: {e}')
#       __             _    _                   _        _                
#      /__\ __ _ _ __ | | _(_)_ __   __ _    __| | ___  (_)_ __ ___   ___ 
#     / \/// _` | '_ \| |/ / | '_ \ / _` |  / _` |/ _ \ | | '_ ` _ \ / __|
#    / _  \ (_| | | | |   <| | | | | (_| | | (_| |  __/ | | | | | | | (__ 
#    \/ \_/\__,_|_| |_|_|\_\_|_| |_|\__, |  \__,_|\___| |_|_| |_| |_|\___|
#                                   |___/                                 
   elif choice == "7":
      try:
         ranking_imc(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar mostrar o ranking de melhores IMCs. Tente novamente! Erro: {e}')

#       ___            _                
#      / __\ __ _  ___| | ___   _ _ __  
#     /__\/// _` |/ __| |/ / | | | '_ \ 
#    / \/  \ (_| | (__|   <| |_| | |_) |
#    \_____/\__,_|\___|_|\_\\__,_| .__/ 
#                                |_|    
   elif choice == "8":
      try:
         listAlunos = backup(listAlunos)
      except Exception as e:
         print(f'Ocorreu um erro ao tentar gerenciar os backups. Tente novamente! Erro: {e}')

#       __                 
#      / /  ___   __ _ ___ 
#     / /  / _ \ / _` / __|
#    / /__| (_) | (_| \__ \
#    \____/\___/ \__, |___/
#                |___/     
   elif choice == "9":
      try:
         logs()
      except Exception as e:
         print(f'Ocorreu um erro ao tentar gerenciar as logs. Tente novamente! Erro: {e}')

#     __       _      
#    / _\ __ _(_)_ __ 
#    \ \ / _` | | '__|
#    _\ \ (_| | | |   
#    \__/\__,_|_|_|   
#                     
   elif choice == "10":
      print('Obrigado por usar o GymSystem desenvolvido pelo n1ck. Volte sempre!')
      sleep(2)
      break

   else:
      print("Opção inválida.")
      




   
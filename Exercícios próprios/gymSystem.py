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

from time import sleep;



#    8888888888                         888    d8b                            
#    888                                888    Y8P                            
#    888                                888                                   
#    8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b  
#    888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K      
#    888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b. 
#    888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88 
#    888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P' 

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
      print('Valor inválido.')
      return

   # Adicionando novo aluno na lista de alunos.
   listAlunos.append(novoAluno)
   print('\nAluno Adicionado com sucesso.')



def listar_alunos(listAlunos):
   print(f"Total de alunos cadastrados: {len(listAlunos)}\n")
   print(f"{'Nome':<15} | {'Plano':<12} | {'Idade':<5} | {'IMC':<6}")
   print("-" * 50)
   for aluno in listAlunos:
      print(f"{aluno['nome']:<15} | {aluno['plano']:<12} | {aluno['idade']:<5} | {aluno['imc']:<6}")



def pesquisar_aluno(listAlunos):
   nameAluno = input('Digite o nome do alunos que deseja encontrar.\n> ')
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
5 - Voltar ao menu
                              
> """)
         try:
            if choiceChange == '1':
               newIdade = int(input('Digite a nova idade.\n> '))
               aluno['idade'] = newIdade
               print('\nIdade alterada.')
            elif choiceChange == '2':
               newPeso = float(input('Digite o novo peso.\n> '))
               aluno['peso'] = newPeso; aluno['imc'] = round(newPeso / (aluno['altura'] ** 2), 2)
               print('\nPeso alterado.')
            elif choiceChange == '3':
               newAltura = float(input('Digite a nova altura.\n> '))
               aluno['altura'] = round(newAltura, 2); aluno['imc'] = round(aluno['peso'] / (newAltura ** 2), 2)
               print('\nAltura alterada.')
            elif choiceChange == '4':
               newPlano = int(input("""Qual o novo plano do aluno?\n\n1 - Mensal\n2 - Trimestral\n3 - Anual\n> """))
               if newPlano == 1:
                  aluno['plano'] = 'Mensal'
                  print('\nPlano alterado com sucesso!')
               elif newPlano == 2:
                  aluno['plano'] = 'Trimestral'
                  print('\nPlano alterado com sucesso!')
               elif newPlano == 3:
                  aluno['plano'] = 'Anual'
                  print('\nPlano alterado com sucesso!')
               else:
                  print('Valor inválido.')
               return
            elif choiceChange == '5':
               return
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
            listAlunos.remove(aluno)
            print('\nAluno removido com sucesso.')
         elif removeChoice == '2':
            continue
         else:
            print('Opção inválida.')
            


def adicionar_treinos(listAlunos):
   return



def remover_treinos(listAlunos):
   return

#    888b     d888                            
#    8888b   d8888                            
#    88888b.d88888                            
#    888Y88888P888  .d88b.  88888b.  888  888 
#    888 Y888P 888 d8P  Y8b 888 "88b 888  888 
#    888  Y8P  888 88888888 888  888 888  888 
#    888   "   888 Y8b.     888  888 Y88b 888 
#    888       888  "Y8888  888  888  "Y88888                         

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
      pass

#       __             _    _                   _        _                
#      /__\ __ _ _ __ | | _(_)_ __   __ _    __| | ___  (_)_ __ ___   ___ 
#     / \/// _` | '_ \| |/ / | '_ \ / _` |  / _` |/ _ \ | | '_ ` _ \ / __|
#    / _  \ (_| | | | |   <| | | | | (_| | | (_| |  __/ | | | | | | | (__ 
#    \/ \_/\__,_|_| |_|_|\_\_|_| |_|\__, |  \__,_|\___| |_|_| |_| |_|\___|
#                                   |___/                                 
   elif choice == "7":
      pass

#       ___            _                
#      / __\ __ _  ___| | ___   _ _ __  
#     /__\/// _` |/ __| |/ / | | | '_ \ 
#    / \/  \ (_| | (__|   <| |_| | |_) |
#    \_____/\__,_|\___|_|\_\\__,_| .__/ 
#                                |_|    
   elif choice == "8":
      pass

#       __                 
#      / /  ___   __ _ ___ 
#     / /  / _ \ / _` / __|
#    / /__| (_) | (_| \__ \
#    \____/\___/ \__, |___/
#                |___/     
   elif choice == "9":
      pass

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
      




   
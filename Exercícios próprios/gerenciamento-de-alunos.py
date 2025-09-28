# Super Desafio Python: Análise de Dados de Alunos

"""
Desafio: Crie um programa completo que:

1. Peça ao usuário para digitar o nome de uma turma (ex: "Turma A").
2. Peça quantos alunos há na turma.
3. Para cada aluno, peça:
   - Nome
   - 2 notas (float)
4. Armazene os dados em uma lista de dicionários, onde cada dicionário representa um aluno.
5. Calcule e mostre:
   a) A média da turma (usando statistics.mean)
   b) O nome do aluno com maior média
   c) O nome do aluno com menor média
   d) Quantos alunos ficaram acima da média da turma
   e) Liste todos os alunos e suas médias, em ordem decrescente de média
6. Pergunte se o usuário quer salvar o resultado em um arquivo .txt (use o módulo os para criar/verificar o arquivo)
7. Se sim, salve o relatório no arquivo com o nome da turma (ex: TurmaA.txt)

Regras:
- Use apenas recursos já vistos nas aulas e nos arquivos de módulos.
- Não use recursos avançados, apenas o que já praticou.
- Use listas, dicionários, laços, input, print, módulos math/statistics/os, etc.
- Não use bibliotecas externas.

Boa sorte!
"""

# Importando aluns módulos built-in.
import statistics; import math; import os

# Criando um looping basico para menus.
while True:

# Criando a turma
   classe = list()
   print('Digite o nome da turma, ex: Turma A')
   continue
   className = input('> ')
   print('\nA turma possue quantos alunos? ')
   alunos = int(input('> '))

# Definindo alunos
   for aluno in range(alunos):
      print(f'\nAluno numero: {aluno + 1}\n')
      nameAluno = input('Nome do aluno: ')
      nota1 = float(input('Primeira nota: '))
      nota2 = float(input('Segunda nota: '))
      classe.append({nameAluno: [nota1, nota2]})


# Variaveis de controle
   relatorio = """Script feito por: Nick
   """
   mean = []
   meanAluno = 0
   meanEqual = False
   c = 0
   listMedias = list()

# Iterando sobre alunos
   for aluno in classe:
      for key, value in aluno.items():

         # Controlando a criação de variaveis.
         if c == 0:
            listAlunosGoodMean = list()
            badMeanAluno = (value[0] + value[1]) / 2

         # Adicionando notas a uma lista, para tirar a media total.
         mean.append(value[0])
         mean.append(value[1])

         # Listando aluno com maior nota
         if (value[0] + value[1]) / 2 > meanAluno:
            meanAluno = (value[0] + value[1]) / 2
            meanNameAluno = key

         # Listando aluno com menor nota
         if (value[0] + value[1]) / 2 <= badMeanAluno:
            badMeanAluno = (value[0] + value[1]) / 2
            badMeanNameAluno = key

         # Listando alunos com media maior que 6.
         if (value[0] + value[1]) / 2 >= 6:
            listAlunosGoodMean.append(key)

         # Adicionando as medias em uma lista de medias
         listMedias.append((key, (value[0] + value[1]) / 2))

         # Incrementando contador para controle de variaveis. Gambiarrakkkkkkkkkkkkkkkkk
         c += 1

   # Imprimindo Media de notas.
   print(f"\nMedia de notas da turma: {statistics.mean(mean) :.1f}")
   relatorio += f"\nMedia de notas da turma: {statistics.mean(mean) :.1f}\n"

   # Imprimindo maior media.
   print(f'{meanNameAluno} obteve a maior media, com {meanAluno :.1f} pontos em media.')
   relatorio += f'{meanNameAluno} obteve a maior media, com {meanAluno :.1f} pontos em media.\n'

   # Imprimindo menor media.
   print(f'{badMeanNameAluno} obteve a menor media, com {badMeanAluno :.1f} pontos em media.')
   relatorio += f'{badMeanNameAluno} obteve a menor media, com {badMeanAluno :.1f} pontos em media.\n'

   # Verificando se existem alunos acima da media, se sim: Mostrando-os.
   if len(listAlunosGoodMean) > 0:
      print("\nAlunos com media acima de 6:")
      relatorio += "\nAlunos com media acima de 6: \n"
      c = 0

      # Iterando sobre alunos com media acima de 6. Para imprimir seus nomes, um de cada vez.
      for aluno in listAlunosGoodMean:
         print(aluno)
         c += 1
      print(f'Total: {c}\n')
      relatorio += f'Total: {c}\n'
   else:
      print("Nenhum aluno com media acima de 6.\n")
      relatorio += "Nenhum aluno com media acima de 6.\n"
   
   # Imprimindo os alunos e suas medias de forma decrescente.
   listMedias.sort(key=lambda x: x[1], reverse=True)
   for tupla in listMedias:
      print(f"{tupla[0]} - Media: {tupla[1]}")
      relatorio += f"{tupla[0]} - Media: {tupla[1]}\n"

   # Questionando sobre o relatorio
   print("""\nDeseja salvar o relatorio em um arquivo txt?

1 - Sim
2 - Não
         """)
   choice = input('> ')

   # Salvando relatorio, ou nao.
   if choice == '1':
      arquivoName = className.replace(' ', '-') + '.txt'
      caminhoArquivo = os.path.join(os.getcwd(), arquivoName)
      arquivo = open(caminhoArquivo, 'w', encoding='utf-8')
      arquivo.write(relatorio)
      arquivo.close()

      print(f"Relatório salvo com sucesso em: {caminhoArquivo}")
   elif choice == '2':
      print("""Deseja adicionar mais turmas?

1 - Sim
2 - Não""")
      choice = input('> ')
      if choice == '1':
         pass
      else:
         break
   else:
      print("Opção inválida. Encerrando programa.")
   break

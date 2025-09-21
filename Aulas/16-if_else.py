name = input('Digite o nome do jogo: ')
yearLaunch = int(input('Digite o ano de lançamento: '))
classification = float(input('Digite a classificação do jogo (0.0 a 10.0): '))

if classification > 8 or yearLaunch > 2015:
    print(f'O jogo {name} é um ótimo jogo!')
else:
    print(f'O jogo {name} é um jogo razoável.')

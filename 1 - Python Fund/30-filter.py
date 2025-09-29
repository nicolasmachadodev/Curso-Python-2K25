# Usamos o filter para iterar sobre itens e retornar aqueles que atendem a condição

idades = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Utilizamos uma function que crie uma condicao usando cada item do iteravel.  E por fim, direcionamos qual iteravel sera usado como base para aplicar o filtro.
menores =list(filter(lambda x: x < 18, idades))

print(menores)

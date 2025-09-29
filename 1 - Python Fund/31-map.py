# Usamos o map para filtrar e alterar valores de um iteravel.

listaNumbers = [i for i in range(1, 16)]

# Transformando numeros menores que 10 em -1, e retornando o valor sem alteracao caso a condicao seja false.
menoresDe10Alterados = list(map(lambda x: -1 if x < 10 else x, listaNumbers))

print(menoresDe10Alterados)
""" Exercicio 3:

        Calculo de distancia:
        > Escrever um programa que pergunte a distancia que um passageiro deseja percorrer em km.
        > Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,35 para viagens mais longas.

"""
distance = float(input("Quantos KM deseja percorrer: "))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.35

print(f"O valor total e de: R${price:.2f}")

"""

        Aumento salarial de funcionários:
        > Escrever um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
        > Para salários superiores a R$1250,00, calcule um aumento de 10%.
        > Para os inferiores ou iguais, o aumento é de 15%.

"""

salario = float(input("Salario atual: "))
if salario > 1250:
    salario *= 1.10
else:
    salario *= 1.15

print(f"Novo salario: R${salario:.2f}")

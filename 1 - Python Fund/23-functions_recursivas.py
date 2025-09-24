def factorial(n):
    """Calcula o fatorial de um número n de forma recursiva."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Digite um número para calcular o fatorial: "))
if number < 1:
    print("Por favor, digite um número inteiro maior ou igual a 1.")
else:
    result = factorial(number)
    print(f"O fatorial de {number} é {result}")

# 2 - Soma total de um número
def sumTotal(n):
    """Calcula a soma total de todos os números de 1 até n de forma recursiva."""
    if n == 1:
        return 1
    else:
        return n + sumTotal(n - 1)
number = int(input("Digite um número para calcular a soma total: "))
if number < 1:
    print("Por favor, digite um número inteiro maior ou igual a 1.")
else:
    result = sumTotal(number)
    print(f"A soma total de 1 até {number} é {result}")
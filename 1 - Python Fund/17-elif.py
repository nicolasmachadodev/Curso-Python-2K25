num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operation = input('Digite a operação (+, -, *, /): ')

if operation == '+':
    result = num1 + num2
    print(f'O resultado de {num1} + {num2} é {result}.')
elif operation == '-':
    result = num1 - num2
    print(f'O resultado de {num1} - {num2} é {result}.')
elif operation == '*':
    result = num1 * num2
    print(f'O resultado de {num1} * {num2} é {result}.')
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f'O resultado de {num1} / {num2} é {result}.')
    else:
        print('Erro: Divisão por zero não é permitida.')
else:
    print('Operação inválida. Por favor, escolha entre +, -, * ou /.')

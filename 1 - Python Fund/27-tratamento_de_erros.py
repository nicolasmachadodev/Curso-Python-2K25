def calcularDivisao(a, b):
    div = a / b
    return div

n1 = 2
n2 = 5

try:
    print(calcularDivisao(n1, n2))
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    print('Encerrando programa.')
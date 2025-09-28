
# 1 - Podemos criar nosso proprio erro com o raise.
def calcSoma(a, b):
    if a < 0 or b < 0:
        raise ValueError("Nao somamos numeros negativos.")
    return print(a + b)

calcSoma(5, 5)

# 2 - Podemos fazer uma verificacao rapida usando o assert
idade = -2

assert idade > 0, "COMO ASSIM IDADE NEGATIVA PORRA"
import math

# 1 - Acesse o valor de pi do módulo math e imprima-o.
print(math.pi)

# 2 - Acesse o valor de e do módulo math e imprima-o.
print(math.e)

# 3 - Arredondando numeros para cima e para baixo
print(math.ceil(4.2))  # Arredonda para cima
print(math.floor(4.7)) # Arredonda para baixo
print(round(4.5))      # Arredonda para o inteiro mais próximo

# 4 - Fatorial
print(math.factorial(5)) # 5! = 5*4*3*2*1 = 120

# 5 - Raiz quadrada
print(math.sqrt(16)) # 4

# 6 - Potência
print(math.pow(2, 3)) # 2^3 = 8

# 7 - Seno, Cosseno e Tangente
print(math.sin(math.pi/2)) # Seno de 90 graus = 1
print(math.cos(0))         # Cosseno de 0 graus = 1
print(math.tan(math.pi/4)) # Tangente de 45 graus = 1

# 8 - Logaritmo
print(math.log(100, 10)) # Logaritmo base 10 de 100
print(math.log(math.e))   # Logaritmo natural de e
print(math.log2(8))      # Logaritmo base 2 de 8
print(math.log10(1000))  # Logaritmo base 10 de 1000

# 9 - MDC (Máximo Divisor Comum) e MMC (Mínimo Múltiplo Comum)
print(math.gcd(48, 18)) # MDC de 48 e 18
print(math.lcm(4, 5))   # MMC de 4 e 5

# 10 - Hipotenusa
print(math.hypot(3, 4)) # Hipotenusa de um triângulo retângulo com catetos 3 e 4
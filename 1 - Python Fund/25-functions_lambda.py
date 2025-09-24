# 1 - Function de potencia de um numero

defPow = lambda num: num ** 2
print(defPow(5))

# 2 - Verifica se o numero é par

defPar = lambda num: num % 2 == 0
print(defPar(2))

# 3 - Function que divide um numero por outro.

defDiv = lambda num, num2: num / num2
print(defDiv(8, 2))

# 4 - Function que inverte uma string

defInvert = lambda word: word[::-1]
print(defInvert('Python'))
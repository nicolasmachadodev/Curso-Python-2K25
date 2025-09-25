"""
* Modulo de strings
-> Escreva um modulo em python para tratar algumas strings e que possua as seguintes funcoes:

1 - Inverter uma string de tras para frente
2 - Retornar apenas letras com indices pares
3 - Retornar apenas letras com indices impares

"""

import strings

newWord = input("Digite uma palavra: ")

print(strings.invert(newWord))
print(strings.par(newWord))
print(strings.impar(newWord))

"""
Exercicio 5:
    > Conta letras maiusculas e minusculas:
        Escreva uma function que recebe uma string como parametro e conta quantas letras maiusculas e minusculas tem.
"""

def wordsM(text):
    upper = lower = 0
    for word in text:
        if word.isupper():
            upper += 1
        elif word.islower():
            lower += 1
    print(f"Maiusculas: {upper}\nMinusculas: {lower}")
            
word = input("Digite uma frase: ")
wordsM(word)

"""
    > Lista de numeros pares e impares:
        Crie uma function para imprimir os numeros pares e impares em duas listas diferentes.
"""

def numberP(*nums):
    par = [num for num in nums if num % 2 == 0]
    impar = [num for num in nums if num % 2 != 0]
    print(f'Pares: {par}\nImpares: {impar}')
    
numberP(3, 6, 4, 135, 234, 657, 43, 2)
"""
Exercicio 4:
    > Contagem Regressiva:
        Faça um programa para escrever a contagem de 10 a 0, ao finalizar, devera emitir um som de "beep".
"""
import winsound
from time import sleep

n = 10
for i in range(11):
    print(n)
    sleep(0.5)
    n -= 1
print('beep!')
winsound.Beep(2000, 400)
"""
Tabuada:
    > Faça um programa que calcule a tabuada de um numero, com o usuario informando o valor inicial e final do numero.
"""

numberSelected = int(input('Numero: '))
firstNumber = int(input('Numero de inicio: '))
lastNumber = int(input('Numero final: '))

if firstNumber < lastNumber:
     for n in range(firstNumber, lastNumber + 1):
          print(f'{numberSelected} X {n} = {numberSelected * n}')

"""
Exercicio 1:
    Escreva um programa que altere todas as ocorrencias que são iguais a primeira, mas não altere a primeira/ Exemplo
    fifa 23 > fi$a 23
"""

name = "fiFA 23"
firstLetter = name[0]
name = name.replace(firstLetter.lower(), "$")
name = name.replace(firstLetter.upper(), "$")
print(f"{firstLetter}{name[1:]}")

"""
Exercicio 2:
    Escreva um programa com duas variaveis para obter uma unica string, onde as duas primeiras letras da variavel sao trocadas, e a ultima é mantida
    
    Exemplo: abc xyz > xyc abz
"""

st1 = "abc"
st2 = "xyz"

newSt1 = st1.replace(st1[0], st2[0])
newSt1 = newSt1.replace(st1[1], st2[1])

newSt2 = st2.replace(st2[0], st1[0])
newSt2 = newSt2.replace(st2[1], st1[1])

print(newSt1, newSt2)
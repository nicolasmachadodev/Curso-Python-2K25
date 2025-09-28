from pympler.asizeof import asizesof

def listaDobro(lista):
    dobro = list()
    for n in lista:
        dobro.append(n * 2)
    return dobro

dobro = listaDobro(range(0, 10000))

def listadobro2(lista):
    for n in lista:
        yield n * 2

dobro2 = listadobro2(range(0, 10000))

while True:
    try:
        print(next(dobro2))
    except StopIteration:
        break

# Args e Kwargs

# 1 - Soma total de numeros. Args

def sumTotal(*num):
    sum = 0
    for number in num:
        sum += number
    print(f"Soma total: {sum}")

sumTotal(5, 7, 2, 10)

# 2 - Info de um produto. Kwargs

def shampoo(**info):
    for key, value in info.items():
        print(f'{key} = {value}')

shampoo(Price=13.90, Stock=37, Name='ClearMan CR7')

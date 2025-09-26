import webbrowser

while True:
    print("""Selecione: 
          
1 - Aprender Python
2 - Aprender sobre módulos
3 - Aprender sobre Python, FullStack JS, Ingles e No Code
4 - Sair""")
    
    choice = input("> ")
    if choice == '1':
        webbrowser.open("https://python.org")
    elif choice == '2':
        webbrowser.open("https://docs.python.org/3/py-modindex.html")
    elif choice == '3':
        webbrowser.open("https://onebitcode.com")
    elif choice == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

import pickle;
from time import sleep;
from datetime import datetime;
from email_validator import validate_email, EmailNotValidError;

def mini_logo():
    print(r"""  __  _      _         __ _                 
 /\ \ \/ | ___| | __    / _\ |_ ___  _ __ ___ 
/  \/ /| |/ __| |/ /    \ \| __/ _ \| '__/ _ \
/ /\  / | | (__|   <     _\ \ || (_) | | |  __/
\_\ \/  |_|\___|_|\_\    \__/\__\___/|_|  \___|
          """)
    
def big_logo():
    sleep(2)
    print(r"""$$\   $$\   $$\            $$\              $$$$$$\    $$\                                   
$$$\  $$ |$$$$ |           $$ |            $$  __$$\   $$ |                                  
$$$$\ $$ |\_$$ |  $$$$$$$\ $$ |  $$\       $$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |  $$ | $$  _____|$$ | $$  |      \$$$$$$\  \_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ 
$$ \$$$$ |  $$ | $$ /      $$$$$$  /        \____$$\   $$ |    $$ /  $$ |$$ |  \__|$$$$$$$$ |
$$ |\$$$ |  $$ | $$ |      $$  _$$<        $$\   $$ |  $$ |$$\ $$ |  $$ |$$ |      $$   ____|
$$ | \$$ |$$$$$$\\$$$$$$$\ $$ | \$$\       \$$$$$$  |  \$$$$  |\$$$$$$  |$$ |      \$$$$$$$\ 
\__|  \__|\______|\_______|\__|  \__|       \______/    \____/  \______/ \__|       \_______|
                                                                                               """)

def listar_produtos(productsList):
    if not len(productsList) > 0:
        print('Nenhum produto cadastrado.')
        return
    print(f"Total de produtos cadastrados: {len(productsList)}\n")
    print(f"{'ID':<5} | {'Nome':<25} | {'Preço':<5} | {'Estoque':<6}")
    print("-" * 50)
    for index, product in enumerate(productsList):
        print(f"{index:<5} | {product['name']:<25} | {product['price']:<5} | {product['stock']:<6}")
    print("-" * 50)

def is_valid_email_library(email):
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False

def save_file(file, data):
    with open(file, 'wb') as arq:
        pickle.dump(data, arq)

def create_files(*names):
    for name in names:
        try:
            with open(name, 'rb') as arq:
                pass
        except:
            with open(name, 'wb') as arq:
                pass
    

def load_file_binary(file):
    try:
        with open(file, 'rb') as arq:
            li = pickle.load(arq)
        return li
    except:
        return []



def login():
    while True:
        big_logo()
        print("""
1 - Fazer login
2 - Realizar cadastro""")
        choice = input('> ')
        if choice == '1':
            if not len(usersList) >= 1:
                print('Nenhum usuário cadastrado.')
                continue
            username = input('Digite seu nome de usuário\n> ')
            for user in usersList:
                if username.lower() == user['user'].lower():
                    password = input('Digite sua senha\n> ')
                    if password == user['password']:
                        print('Login realizado com sucesso!')
                        return user
                    else:
                        print('Senha incorreta.')
            print('Usúario não encontrado.')

        elif choice == '2':
            email = input('Digite seu e-mail\n> ')
            if not is_valid_email_library(email):
                print('E-mail inválido.')
                continue
            
            user = input('Crie um nome de usuário\n> ')
            for usuario in usersList:
                if usuario['user'].lower() == user.lower():
                    print('Usuário já existente.')
                    continue

            for usuario in usersList:
                if usuario['email'].lower() == email.lower():
                    print('E-mail já existente.')
                    continue

            password = input('Digite sua senha\n> ')
            passwordVerify = input('Digite novamente\n> ')
            if password != passwordVerify:
                print('As senhas não coincidem.')
                continue

            if user == 'admin':
                usersList.append({'user': user, 'email': email, 'password': password, 'admin': True})
            else:
                usersList.append({'user': user, 'email': email, 'password': password, 'admin': False})
            save_file('users.pkl', usersList)
            print('\nUsuário cadastrado com sucesso.')

        elif choice not in ['1', '2']:
            print('Escolha inválida.')

def client_menu():
    return

def admin_menu(admin):
    productsList = load_file_binary('products.pkl')
    while True:
        big_logo()
        print(r"""                -  -  -  -  -  -  - MENU ADMIN  -  -  -  -  -  -  -        

1 - Gerenciar Produtos
2 - Histórico de vendas
3 - Relatórios
4 - Gerenciar usuários
        """)

        choice = input('> ')

        if choice == '1':
            mini_logo()
            print("""                              
1 - Cadastrar novo produto
2 - Editar produto
3 - Excluir produto
4 - Listar todos os produtos (Obter ID)
5 - Voltar
""")
            choice = input("> ")
            if choice == '1':
                productName = input('Digite o nome do produto: ')
                productCategory = input('Digite a categoria do produto: ')
                try:
                    productPrice = float(input('Digite o valor do produto. Exemplo: "15.99": '))
                except:
                    print('Insira um valor válido.')
                    continue
                try:
                    productStock = int(input('Digite a quantidade em estoque: '))
                except:
                    print('Insira um valor válido.')
                    continue
                productsList.append({'name': productName, 'category': productCategory, 'price': productPrice, 'stock': productStock})
                save_file('products.pkl', productsList)


            elif choice == '2':
                try:
                    index = int(input('Digite o ID do produto desejado: '))
                except:
                    print('ID inválido.')
                    continue
                if index < len(productsList) and index >= 0:
                    print(f"Produto encontrado.\n\n{'ID':<5} | {'Nome':<25} | {'Preço':<5} | {'Estoque':<6}")
                    print("-" * 50)
                    print(f"{index:<5} | {productsList[index]['name']:<25} | R$ {productsList[index]['price']:<5} | {productsList[index]['stock']:<6}")
                    print("-" * 50)
                    choice = input('\nO que deseja editar?\n1 - Nome\n2 - Categoria\n3 - Estoque\n4 - Preço\n> ')

                    if choice == '1':
                        newName = input('Digite um novo nome para o produto\n> ')
                        productsList[index]['name'] = newName
                        print('Nome alterado com sucesso!')
                    elif choice == '2':
                        newName = input('Digite uma nova categoria para o produto\n> ')
                        productsList[index]['category'] = newName
                        print('Categoria alterada com sucesso!')
                    elif choice == '3':
                        try:
                            newName = int(input('Digite uma nova quantidade de estoque para o produto\n> '))
                        except:
                            print('Valor inválido.')
                        
                        productsList[index]['stock'] = newName
                        print('Estoque modificado com sucesso!')
                    elif choice == '4':
                        try:
                            newName = float(input('Digite um novo preço para o produto\n> '))
                        except:
                            print('Valor inválido.')
                        productsList[index]['price'] = newName
                        print('Preço alterado com sucesso!')
            elif choice == '3':
                try:
                    index = int(input('Digite o ID do produto desejado: '))
                except:
                    print('ID inválido.')
                    continue
                if index < len(productsList) and index >= 0:
                    print(f"Produto encontrado.\n\n{'ID':<5} | {'Nome':<25} | {'Preço':<5} | {'Estoque':<6}")
                    print("-" * 50)
                    print(f"{index:<5} | {productsList[index]['name']:<25} | R$ {productsList[index]['price']:<5} | {productsList[index]['stock']:<6}")
                    print("-" * 50)
                    choice = input('\nO que deseja fazer?\n1 - Excluir produto\n2 - Voltar\n> ')

                    if choice == '1':
                        productsList.remove(productsList[index])
                        print('Produto removido com sucesso!')
                    elif choice == '2':
                        continue
                    else:
                        print('Escolha inválida.')
            elif choice == '4':
                listar_produtos(productsList)
            elif choice == '5':
                continue
            else:
                print('Opção inválida.')

        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print('Opção inválida.')

create_files('users.pkl', 'products.pkl', 'vendas.pkl', 'backup.pkl')
usersList = load_file_binary('users.pkl'); activeUser = login();
print(f'Seja bem vindo(a): {activeUser['user'].capitalize()}')

if activeUser['admin']:
    admin_menu(activeUser)

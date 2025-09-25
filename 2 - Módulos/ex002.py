"""
Agendar o desligamento do pc em uma hora e em meia hora.
"""
import os

def powerOff1hour():
    os.system('shutdown -s -t 3600')

def powerOff30minutes():
    os.system('shutdown -s -t 1800')

def cancelPowerOff():
    os.system('shutdown -a')

while True:
    print("""Selecione: 

1 - Desligar o pc em 1 hora
2 - Desligar o pc em 30 minutos
3 - Sair
          """)
    choice = int(input('> '))
    if choice == 1:
        powerOff1hour()
        while True:
            print("""Deseja cancelar?

1 - Sim
2 - Não
                  """)
            choiceTwo = int(input("> "))
            if choiceTwo == 1:
                cancelPowerOff()
                break
            elif choiceTwo == 2:
                pass
            else:
                print("Opção inválida.")
    elif choice == 2:
        powerOff30minutes()
        while True:
            print("""Deseja cancelar?

1 - Sim
2 - Não
                  """)
            choiceTwo = int(input("> "))
            if choiceTwo == 1:
                cancelPowerOff()
                break
            elif choiceTwo == 2:
                pass
            else:
                print("Opção inválida.")
    elif choice == 3:
        break
    else:
        print("Opção inválida.")


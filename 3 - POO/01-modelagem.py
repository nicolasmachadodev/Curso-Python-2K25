class Pessoas:

    vivo = True
    possui_olho = True
    possui_boca = True
    raca = "Humana"

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def return_name(self):
        return self.nome

    def logar_sistema(self):
        print(f"{self.return_name()} esta logando no sistema.")

p1 = Pessoas('Nicolas', 16, 10415218985)
p2 = Pessoas('Emilly', 17, 68638361904)

p1.logar_sistema()

print(p2.idade)

Pessoas.vivo = False

print(p1.vivo)

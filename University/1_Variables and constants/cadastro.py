print("Bem vindo ao cadastro!\n")
print("\n")

nome = input("Digite seu nome: \n")
idade = input("Digite sua idade: \n")
cidade = input("Digite sua cidade: \n")
ativo = input("Voce é ativo ? \n")

ativo = ativo.lower() == "s"

print("Me chamo", nome,"Tenho", idade, "sou da", cidade,"e sou", ativo)
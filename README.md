


import getpass
import csv
from conta import Conta

contas = []
with open('contas.csv', newline = '', encoding = 'utf-8', errors = 'ignore') as lerContas:
    leitor = csv.reader(lerContas, delimiter = ',')
    for linha in leitor:
        conta = Conta(linha[0], linha[1],linha[2],linha[3], linha[4])
        contas.append(conta)

print(contas[0].agencia)

agencia = int(input("Digite a agência: "))
numero_conta = int(input("Digite sua conta corrente: "))
senha = getpass.getpass("Digite a senha: ")

print(agencia,numero_conta, senha)

# Encontrar a conta corrente na lista de contas
contaEncontrada = None
for conta in contas:
    if numero_conta == conta.numero:
        contaEncontrada = Conta(conta.agencia, conta.numero, conta.titular, conta.saldo, conta.senha)

if contaEncontrada == None: # verifica se a conta é Nula (inexistente)
    print("Dados incorretos")
else:
    # Verificar se o usuário digitou a senha e agencia corretamente
    if senha == contaEncontrada.senha and agencia == contaEncontrada.__agencia:
       print("Acesso liberado")
    else:
        print("Dados incorretos")

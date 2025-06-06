import random
import getpass
from conta import Conta

import csv
def escreveArquivo(agencia, numero, titular, saldo, senha):
    with open('contas.csv', 'a', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter= ',')
        escritor.writerow([agencia, numero, titular, saldo, senha])
        
    

while(True):
    print("### CADASTRO DE CONTA BANCÁRIAS - BANCO VAI LÉO ###")
    print("preencha os seguintes dados: ")
    agencia = int(input("Número da agencia: "))
    numero = random.randint(10000, 99999)
    titular = input("Nome completo do cliente: ")
    saldo = float(input("Saldo inicial: "))
    senha = getpass.getpass("Solicite uma nova senha:")
    escreveArquivo(agencia, numero, titular, saldo, senha)
    novaConta = Conta(agencia, numero, titular, saldo,)
    print(f'Conta cadastrada com sucesso!/n Número da conta {novaConta.numero}/n')
def sacar():
    saldo = 1350
    valor = int(input("Digite um valor para sacar: "))
    
    if (valor > saldo):
        print("Erro ao sacar: saldo insuficiente.")
    else:
        print("Saque realizado com sucesso.")

sacar()
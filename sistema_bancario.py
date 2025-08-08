saldo_conta         = 0
quantidade_de_saque = 0
limite_diario       = 0
usuarios = []


def criar_conta():
    nome            = input("Digite seu nome: ")
    cpf             = input("Digite seu cpf: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    
    if len(cpf) == 11 and cpf.isdigit():
       
        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        
    else:
       
        print("CPF INVÁLIDO.")
        return
    
    if len(data_nascimento) == 8 and data_nascimento.isdigit():
       
        data_nascimento_formatada = f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
        ano_nascimento = int(data_nascimento[4:])
        
    else:
       
        print("Data de nascimento inválida. Use o formato DDMMAAAA.")
        return
    
    ano_atual = 2025
    idade     = ano_atual - ano_nascimento
   
    
    if idade < 18:
        print("Abertura de conta cancelada, você é menor de idade!")
        return  # impede criação da conta
    
            
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento_formatada
    }
     
    usuarios.append(usuario)
    print("Conta criada com sucesso!")
    print(usuario)
    
    
    
    
def deposito():

    global saldo_conta
    valor = int(input("Digite um valor à ser depositado:"))

    if(valor < 0):
        
        print("Erro no deposíto, efetuar valores maiores que zero")
        
    else:
        saldo_conta += valor
        print(f"Valor depositado: {valor:.2f}")
        


       
def saque():
    global saque
    global saldo_conta
    global quantidade_de_saque
    global limite_diario

    valor = int(input("Digite o valor do saque: "))

    if quantidade_de_saque >= 3:
        
        print("Erro: Limite de saques diários atingido.")
        
    elif valor > 500:
        
        print(f"Erro: O limite por saque é R$500")
        
    elif valor > saldo_conta:
        
        print("Erro: Saldo insuficiente.")
        
    elif valor <= 0:
        
        print("Erro: Valor inválido para saque.")
        
    else:
        saldo_conta -= valor
        quantidade_de_saque += 1
        limite_diario += valor
        print(f"Saque realizado com sucesso: R${valor:.2f}")
        print(f"Saldo restante: R${saldo_conta:.2f}")
        
criar_conta()
        
# deposito()
# # Corrigindo a condição do while
# while quantidade_de_saque < 3 and limite_diario < 500:
#     saque()

# # Exibe o total de saque diário
# print(f"Total sacado no dia: R${limite_diario:.2f}")


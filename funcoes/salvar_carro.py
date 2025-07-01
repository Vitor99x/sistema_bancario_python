def salvar_carro(nome, modelo, ano, placa):
    placa = placa[:3] + '-' + placa[3:]
    print(f"Carro inserido com sucesso: {nome} - {modelo} - {ano} - {placa}")
    
    
# nome_carro = input("Digite o nome do carro: ")
# modelo     = input("Digite o modelo do carro: ")
# ano        = int(input("Digite o ano do carro: "))
# placa      = input("Digite a placa do carro: ")

# salvar_carro(nome_carro, modelo, ano, placa)
salvar_carro(nome="Palio", modelo="Fiat", ano="2022", placa="DLT874")

    """
    FUNÇAO REBENDO UM DICIONARIO "CHAVE" : "VALOR
    """
    
salvar_carro(**{"nome": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC1E76"}) 

    
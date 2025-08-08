# Entrada do usuário
email = input().strip()

# Definir os domínios válidos
dominios_validos = ["gmail.com", "outlook.com"]

# Verificar se o e-mail contém o caractere "@" e não começa com ele
if "@" in email and not email.startswith("@"):
    # Separar o e-mail em parte local e domínio
    usuario, dominio = email.split("@")
    
    # Verificar se o domínio é válido
    if dominio in dominios_validos:
        print("E-mail válido")
    else:
        print("Email inválido: domínio inválido")
else:
    print("E-mail inválido")

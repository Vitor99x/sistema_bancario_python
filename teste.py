descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Digite o preço: ").strip())
cupom = input("Digite o cupom de desconto: ").strip()

# Verificação do cupom
if cupom in descontos:
    desconto = preco * descontos[cupom] 
    preco = preco - desconto
    print(f"Preço com desconto: {preco:.2f}")
else:
    print("Cupom inválido!")
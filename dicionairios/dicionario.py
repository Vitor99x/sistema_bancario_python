pessoa = {"nome" : "Vitor", "idade": 28}

pessoa = dict(nome="Vitor", idade = 25)

pessoa["telefone"] = "4002-8922"

print(pessoa["nome"])


contatos = {
    "vitor@silva.com"   :{"nome": "Vitor",   "Telefone": "4002-8922"},
    "carlos@silva.com"  :{"nome": "Carlos",  "Telefone": "123-8922"},
    "matheus@silva.com" :{"nome": "matheus", "Telefone": "321-8922"},
    "danilo@silva.com"  :{"nome": "danilo",  "Telefone": "132-8922", "extra": {"a": 1}},
}



# print(contatos["vitor@silva.com"]["Telefone"])
extra = contatos["danilo@silva.com"]["extra"]
# print(extra)


# for chave in contatos:
    
#     # print(chave, contatos[chave])
    
    
for chave, valor in contatos.items():
    print(chave, valor)
    
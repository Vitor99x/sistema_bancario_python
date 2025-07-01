contatos = {
    "vitor@silva.com"   :{"nome": "Vitor",   "Telefone": "4002-8922"},
}

# contatos["chave"]


contatos.get("chave")
contatos.get("chave", {})
a = contatos.get("vitor@silva.com", {})

print(a)
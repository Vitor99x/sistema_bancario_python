
contatos = {
    "vitor@silva.com"   :{"nome": "Vitor",   "Telefone": "4002-8922"},
    "carlos@silva.com"  :{"nome": "Carlos",  "Telefone": "123-8922"},
    "matheus@silva.com" :{"nome": "matheus", "Telefone": "321-8922"},
    "danilo@silva.com"  :{"nome": "danilo",  "idade": 25, "Telefone": "132-8922", "extra": {"a": 1}},
}

del contatos["vitor@silva.com"]["Telefone"]
del contatos["danilo@silva.com"]

print(contatos)
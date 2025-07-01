contatos = {
    "vitor@silva.com"   :{"nome": "Vitor",   "Telefone": "4002-8922"},
}

contatos.update({"vitor@silva.com"   :{"nome": "Vitor"}})

contatos.setdefault("idade", 25)
print(contatos)
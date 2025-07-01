contatos = {
    "vitor@silva.com"   :{"nome": "Vitor",   "Telefone": "4002-8922"},
}

contatos.pop("vitor@silva.com")
print(contatos)
resultados = contatos.pop("vitor@2silva.com", "não encontrou")

print(resultados)
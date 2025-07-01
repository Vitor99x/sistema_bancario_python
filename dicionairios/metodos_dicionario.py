contatos = {
    "vitor@silva.com"   :{"nome": "Vitor",   "Telefone": "4002-8922"},
}

copia = contatos.copy()
copia["vitor@silva.com"] = {"nome" : "Hugo"}


print(copia)
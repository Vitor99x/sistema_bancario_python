"""
data_extenso
Tipo esperado: str (string)
O que representa: a data no formato extenso (ex: "Sexta-Feira, 27 de junho de 2025")
Uso na função: aparece no topo da mensagem formatada, como "cabeçalho".

*args
Tipo esperado: uma sequência de strings (tupla de str)
Internamente, o Python agrupa os argumentos posicionais extras em uma tupla.
Exemplo: se você chamar a função com "linha 1", "linha 2", então args será ("linha 1", "linha 2").
O que representa: os versos do poema.
Uso na função: cada elemento de args é considerado uma linha/verso e é unido com "\n".join(args) para formar o corpo do poema.

**kwargs
Tipo esperado: um dicionário de pares chave=valor (dict[str, Any])
Exemplo de chamada: author="Tim Petters", ano=1999
Isso cria: kwargs = {"author": "Tim Petters", "ano": 1999}
O que representa: metadados do poema, como autor, ano, localização, etc.
Uso na função: os pares são formatados como "Chave: Valor" e unidos por quebras de linha.

    
"""

def exibir_poema(data_extenso, *args, **kwargs):
    
    texto       = "\n".join(args)
    meta_dados  = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem    = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Sexta-Feira, 27 de junho de 2025",
             "A vida é breve, mas a arte é longa.",
             "Sonhos são rascunhos da alma.",
             "O silêncio às vezes grita verdades.",
             "Cada passo é um poema não escrito.",
             "No caos também há beleza escondida.",
             "Palavras são pontes entre corações.",
             author="Tim Petters",
             ano=1999)
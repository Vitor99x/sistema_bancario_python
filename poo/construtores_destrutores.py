class Pet:
    def __init__(self, nome, raca, cor, idade):
        print("Inicializando a Classe...")
        self.nome  = nome
        self.raca  = raca
        self.cor   = cor
        self.idade = idade
        
    def __del__(self):
        print("Removendo a instância da Classe...")
        
    def falar(self):
        print("Auauauau")
        
    
c = Pet("Orion", "Pitbull", "marrom/preto", 8)
del c #removendo a classe antes de finaliazr
c.falar()
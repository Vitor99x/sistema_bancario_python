class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def latir(self):
        print("AuAu")
        
    def dormir(self):
        self.acordado=False
        print("Zzzzz...")
    
    
cao_1 = Cachorro("Orion", "Preto/Marrom", "True")
print(cao_1.nome)
print(cao_1.cor)
cao_1.dormir()
print(cao_1.acordado)
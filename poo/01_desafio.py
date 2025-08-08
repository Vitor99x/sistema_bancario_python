class Bicicleta:
    ##CONSTRUTOR DA CLASSE
    def __init__(self, cor, modelo, ano, valor):
        self.cor    = cor
        self.modelo = modelo
        self.ano    = ano
        self.valor  = valor
        # self.marcha = marcha
        
    def buzinar(self):
        print("Plim PLim") 
        
    def parar(self):
        print("Parando bicicleta")      
        print("bicicleta parada")
        
    def correr(self):
        print("Vrummmm...")
               
    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
 
    #transformando os atributos da classe em uma lista acessando o nome da classe e percorrendo um dicionario
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    # def trocar_marcha(self, nmr_marcha):
    #     print("Trocando marcha")
        
    #     def _trocar_marcha():
    #         if nmr_marcha > self.marcha:
    #             print("Marcha trocada....")
                
    #         else:
    #             print("Não foi possível trocar de marcha....")
                

b1 = Bicicleta("Azul", "Rock-Ryder", "2022","3000")
# b1.buzinar()
# b1.parar()
# b1.correr()

b2 = Bicicleta("Preta", "bmx", 2025, 1200)
 

# print(b1.cor, b1.modelo, b1.ano, b1.valor)

print(b2)
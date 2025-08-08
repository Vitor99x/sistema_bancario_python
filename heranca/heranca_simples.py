class Veiculo:
    def __init__(self, cor, modelo, ano, placa):
        self.cor    = cor
        self.modelo = modelo
        self.ano    = ano
        self.placa  = placa 
    
    def ligarMotor(self):
        print(f"motor do veiculo ({self.__class__.__name__}) ligado")

class Motocicleta(Veiculo):
    def trocarOleo(self):
        tipoOleo = input("Qual Óleo você deseja? 1- YAMALLUBE || 2 - CASTROL || 3 - MOTUL: ")
        if (tipoOleo == "1"):
            
            print("Colocando óleo yamalubee")
            print("blu blu blu...")
            print("termino")
            
        elif (tipoOleo == "2"):
            
            print("Colocando óleo castrol")
            print("blu blu blu...")
            print("termino")
            
        elif (tipoOleo == "3"):
            
            print("Colocando óleo motul")
            print("blu blu blu...")
            print("termino")
            
        else:
            
            print("Opção inválida")
            
       

class Caminhao(Veiculo):
    def __init__(self, cor, modelo, ano, placa, carregado):
        super().__init__(cor, modelo, ano, placa)
        self.carregado = carregado
        
    def seguirRota(self):
        print("Inciando rota")
        

class Carro(Veiculo):
    def limparCarro(self):
        print("Limpando carro...")

moto = Motocicleta("preta", "speed", "2025", "DLT1E76")
# moto.ligarMotor()
# moto.trocarOleo()

caminhao = Caminhao("Cinza", "truck", "2023", "BLW3X44","True")
# caminhao.ligarMotor()
# caminhao.seguirRota()


carro = Carro("Vermelho", "sedan","2025", "BMW8E44")
# # carro.ligarMotor()
# # carro.limparCarro()
# carro.limparCarro()
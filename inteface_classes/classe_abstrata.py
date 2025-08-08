from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        
    def desligar(self):
        print("Desligando a TV")
        
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o AR-CONDICIONADO")
        
    def desligar(self):
        print("Desligando O  AR-CONDICIONADO")
        
    def marca(self):
        return "samsung"
        
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca())

controleAR= ControleArCondicionado()
controleAR.ligar()
controleAR.desligar()
print(controleAR.marca())

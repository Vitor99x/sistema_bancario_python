"""
na herança multipla, estamos definindo a classe Animal, criando um ToString para exibir ao invés do nome da clase, exibir os atributos/valores
estou herdando na classe do Ornitorrinco: a classe do Mamifero, sendo assim a classe do Mamifero herda da classe animal, e com isso deve colcoar os atributos de todas classes que você está herdando! se quiser também você pode colocar novos atributos na classe do ornitorrinco


"""

class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        self.cor_do_pelo = cor_do_pelo
        super().__init__(**kw)
        
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_do_pelo, nmr_patas):
        super().__init__(cor_do_pelo = cor_do_pelo, cor_bico = cor_bico, nmr_patas = nmr_patas)

ornitorrinco = Ornitorrinco(nmr_patas = 4, cor_do_pelo = "Vermelho", cor_bico = "laranja")
print(ornitorrinco)

gato = Gato(nmr_patas =  4, cor_do_pelo="Preto")
print(gato)


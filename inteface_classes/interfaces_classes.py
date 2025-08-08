class Estudante:
    escola = "UNIP"
    
    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula
        
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self. escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
        
"""
EXIBINDO OS VALORES CONFORME VOI ATRIBUIDO NAS VARIAVES DE CLASSE/ FUNÇÃO
"""
    
aluno1 = Estudante("Vitor", "N063858")
aluno2 = Estudante("Carlos", "C063800")
mostrar_valores(aluno1, aluno2)

"""
EXIBINDO OS VALORES ALTERADOS DA CLASSE E DO ATRIBUTO DA MATRICULA QUE SERIA DO CONSTRUTOR DA CLASSE E NÃO DA CLASSE
"""

aluno1.matricula = "N06"
Estudante.escola = "FIAP"
mostrar_valores(aluno1, aluno2)


 #É SEMPRE BOM LEMBRAR QUE AS VARIAVEIS DA CLASSE É ALGO UNICO, QUE IRÁ ALTERAR  TODO O ESCOPO 
   

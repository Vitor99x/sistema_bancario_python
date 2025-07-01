"""
NÃO NOMEADO / NOMEADO podendo ser também não nomeado

"""

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Modelo: {modelo} Ano: {ano} Placa: {placa} \nMarca: {marca} Motor: {motor} Combustível: {combustivel}")
    
    
criar_carro("911", 2025, "DLT-1E88", marca="Porche", motor="4.0", combustivel="Podium")
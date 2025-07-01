# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input("").strip())

# Loop para armazenar participantes e seus temas
for _ in range(n):
    entrada = input("").strip()
    nome, tema = map(str.strip, entrada.split(' '))  

    if tema not in eventos:
        eventos[tema] = []  
    eventos[tema].append(nome)  

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {' '.join(participantes)}")

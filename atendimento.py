# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def prioridade(paciente):
    nome, idade, status = paciente
    if status == "urgente":
        return 0  # Maior prioridade
    elif idade > 60:
        return 1  # Segunda prioridade
    else:
        return 2  # Menor prioridade

# Ordena os pacientes com base na prioridade
pacientes.sort(key=prioridade)

# Exibe a ordem de atendimento
nomes_em_ordem = [paciente[0] for paciente in pacientes]
print("Ordem de Atendimento:", ", ".join(nomes_em_ordem))


# TODO: Exiba a ordem de atendimento com título e vírgulas:
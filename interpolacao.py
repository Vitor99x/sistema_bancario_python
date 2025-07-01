nome      = input("Digite seu nome:")
idade     = int(input("Digite sua idade:"))
profissao = input("Digite sua Profissão:")
linguagem = input("Digite sua Linguagem preferida:")

print("Olá, eu me chamo %s. Eu tenho %d anos de idade, trabolho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))


print("Olá, me chamo {}. eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(nome, idade, profissao, linguagem))

print(f"oá, me chamo {nome}. eu tenho {idade} anos de idade, tabalho como {profissao} e estou matriculado no curso de {linguagem}")


pi = 3.14159

print(f"valor de pi: {pi:.2f}")


#acrescentando espaços no print ----------3.14
print(f"valor de pi: {pi:10.2f}")


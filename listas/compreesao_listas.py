numeros = [1, 30, 45, 25, 22, 8, 4, 10]
pares   = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares2 = [numero for numero in numeros2 if numero %2 == 0] 
print(pares2)
        
print(pares)
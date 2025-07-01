def calculadora(operacao):
    
    nm1 = float(input("Digite o primeiro valor"))
    nm2 = float(input("Digite o segundo valor"))
    
    if(operacao == "+"):
        
         soma = nm1 + nm2
         print(f"Soma realizada: {soma}")
         
    elif(operacao == "/"):
        
         soma = nm1 / nm2
         print(f"Divisão realizada: {soma}")
         
    elif(operacao == "*"):
        
         soma = nm1 * nm2
         print(f"Multiplicação realizada: {soma}")
         
    elif(operacao == "-"):
        
         soma = nm1 - nm2
         print(f"Subtração realizada: {soma}")
         
    else:
        print("Opçao Inválida")
       
calculadora("*")
        
        
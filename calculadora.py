print(" ------ | Menu Calculadora | ------\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite 0 para sair e 5 para encerrar")
print("-"*36)
iniciar = int(input("Digite uma opção: "))
while iniciar !=0:
    if iniciar == 1:
        print("--------- | SOMA | --------")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número: "))
        print("-"*35)
        print(f"O resultado é {num1+num2}.")
        print("-"*35)
    elif iniciar == 2:
        print("--------- | SUBTRAÇÃO | --------")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número: "))
        print("-"*35)
        print(f"O resultado é {num1-num2}.")
        print("-"*35)
    elif iniciar == 3:
        print("--------- | MULTIPLICAÇÃO | --------")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número: "))
        print("-"*35)
        print(f"O resultado é {num1*num2}.")
        print("-"*35)    
    elif iniciar == 4:
        print("--------- | DIVISÃO | --------")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número: "))
        print("-"*35)
        print(f"O resultado da divisão é {num1/num2}.")
        print("-"*35)
    elif iniciar == 0:
        print("Saindo...")
        break
    elif iniciar == 5:
        break
    else: 
        print("Número inserido é inválido.")
    print(" ------ | Menu Calculadora | ------\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite 0 para sair e 5 para encerrar")
    print("-"*50)
    iniciar = int(input("Digite uma opção: "))
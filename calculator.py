#bibliotecas para comandos do sistema
import os
import sys
#biblioteca para aplicações de tempo
import time

#função para testar se a string se encaixa em float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
#função de adição
def adição():
    #declaração da resposta base
    ans = 0
    num = input("Digite o primeiro número: ")
    if is_number(num):
        ans += float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o primeiro número: ")
        if is_number(num):
            ans += float(num)
        else:
            print("caractere inválido")

    num = input("Digite o segundo número: ")
    if is_number(num):
        ans += float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o segundo número: ")
        if is_number(num):
            ans += float(num)
        else:
            print("caractere inválido")

    print(f"Resultado: {ans}")
    op2 = input("Você deseja adicionar mais um número ao resultado?\n1- Sim\n2- Não\nResposta: ")
    
    #laço de repetição para adição dos valores consecutivos
    while(op2 != '2'):
        print(f"Resultado: {ans}")
        op2 = input("Você deseja adicionar mais um número ao resultado?\n1- Sim\n2- Não\nResposta: ")
        
        if(op2 == '1'):
            num = input("Digite o número que você deseja adicionar: ")
            if(is_number(num)):
                ans += float(num)
                print(f"Resultado: {ans}")
                op2 = input("Você deseja adicionar mais um número ao resultado?\n1- Sim\n2-Não\nResposta: ")
            else:
                print("Caractere inválido")
                os.system("pause")
        else:
            print("Caractere inválido")
            os.system("pause")
            os.system("cls")

def subtração():
    #declaração da resposta base
    ans = 0
    num = input("Digite o primeiro número (minuendo): ")
    if is_number(num):
        ans += float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o primeiro número (minuendo): ")
        if is_number(num):
            ans += float(num)
        else:
            print("caractere inválido")

    num = input("Digite o número que irá subtrair o anterior (subtraendo): ")
    if is_number(num):
        ans -= float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o número que irá subtrair o anterior (subtraendo): ")
        if is_number(num):
            ans -= float(num)
        else:
            print("caractere inválido")

    print(f"Resultado: {ans}")
    op2 = input("Você deseja subtrair mais um número do resultado?\n1- Sim\n2- Não\nResposta: ")

    #laço de repetição para subtração dos valores consecutivos
    while(op2 != '2'):
        if(op2 == '1'):
            num = input("Digite o número que você deseja subtrair do resultado: ")
            if(is_number(num)):
                ans -= float(num)
                print(f"Resultado: {ans}")
                op2 = input("Você deseja adicionar mais um número ao resultado?\n1- Sim\n2-Não\nResposta: ")
            else:
                print("Caractere inválido")
                os.system("pause")
        else:
            print("Caractere inválido")
            os.system("pause")

def multiplicação():
    #declaração da resposta base
    ans = 0
    #multiplicação dos valores
    ans += float(input("Digite o primeiro número: "))
    ans *= float(input("Digite o segundo número: "))
    print(f"Resultado: {ans}")
    op2 = input("Você deseja multiplicar mais um número ao resultado?\n1- Sim\n2- Não\nResposta: ")
    #laço de repetição para multiplicação dos valores consecutivos
    while(op2 != '2'):
        ans *= float(input("Digite o número que você deseja multiplicar: "))
        print(f"Resultado: {ans}")
        op2 = input("Você deseja multiplicar mais um número ao resultado?\n1- Sim\n2-Não\nResposta: ")
def divisão():
    #declaração da resposta base
    ans = 0
    #divisão dos valores
    ans += float(input("Digite o primeiro número (dividendo): "))
    ans /= float(input("Digite o número que irá dividir o anterior (divisor): "))
    print(f"Resultado: {ans}")
    op2 = input("Você deseja dividir o resultado por mais um número?\n1- Sim\n2- Não\nResposta: ")
    #laço de repetição para adição dos valores consecutivos
    while(op2 != '2'):
        ans /= float(input("Digite o divisor que você deseja: "))
        print(f"Resultado: {ans}")
        op2 = input("Você deseja dividir o resultado por mais um número?\n1- Sim\n2-Não\nResposta: ")
def potência():
    #declaração da resposta base
    ans = 0
    #adição dos valores
    ans += float(input("Digite o primeiro número (base): "))
    ans **= float(input("Digite a potência do número anterior (expoente): "))
    print(f"Resultado: {ans}")
    op2 = input("Você deseja potenciar mais um número ao resultado?\n1- Sim\n2- Não\nResposta: ")
    #laço de repetição para adição dos valores consecutivos
    while(op2 != '2'):
        ans **= float(input("Digite o número que você deseja potenciar o resultado: "))
        print(f"Resultado: {ans}")
        op2 = input("Você deseja potenciar mais um número ao resultado?\n1- Sim\n2-Não\nResposta: ")

#Função Principal
def calculadora():
    op = input("Qual operação você deseja realizar?\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potência\n6- Sair\nResposta: ")
    
    if(op == '1'):
        adição()
    elif(op == '2'):
        subtração()
    elif(op == '3'):
        multiplicação()
    elif(op == '4'):
        divisão()
    elif(op == '5'):
        potência()
    elif(op == '6'):
        print("Exiting program...")
        os.system("pause")

        sys.exit(0)
    else:
        print("Caractere Inválido")
        os.system("pause")
    
    while(op != 6):
        op = input("Qual operação você deseja realizar?\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potência\n6- Sair\nresposta: ")
        if(op == '1'):
            adição()
        elif(op == '2'):
            subtração()
        elif(op == '3'):
            multiplicação()
        elif(op == '4'):
            divisão()
        elif(op == '5'):
            potência()
        elif(op == '6'):
            print("Exiting program...")

            os.system("exit")
            break
        else:
            print("Caractere Inválido")
            os.system("pause")

calculadora()
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
    #atribuição de do valor inserido a uma variável para teste de validez
    num = input("Digite o primeiro número: ")
    if is_number(num):
        ans += float(num)
    else:
        print("caractere inválido")
    #caso seja inserido um caractere inválido, o laço repete até que seja
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
    #print do valor resultante e opção de adicionar mais valores ao resultado
    print(f"Resultado: {ans}")
    op2 = input("Você deseja adicionar mais um número ao resultado?\n1- Sim\n2- Não\nResposta: ")
    #laço de repetição para adição dos valores consecutivos, que é ativado ao ter uma resposta diferente de '2'
    while(op2 != '2'):
        #caso a resposta seja '1', então há um laço para que se repita diversas operaçoes até que o usuário decida parar
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
            print(f"Resultado: {ans}")
            op2 = input("Você deseja adicionar mais um número ao resultado?\n1- Sim\n2- Não\nResposta: ")
#função de subtração
def subtração():
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

    while(op2 != '2'):
        if(op2 == '1'):
            num = input("Digite o número que você deseja subtrair do resultado: ")
            if(is_number(num)):
                ans -= float(num)
                print(f"Resultado: {ans}")
                op2 = input("Você deseja subtrair mais um número do resultado?\n1- Sim\n2-Não\nResposta: ")
            else:
                print("Caractere inválido")
                os.system("pause")
        else:
                print("Caractere inválido")
                os.system("pause")
                os.system("cls")
                print(f"Resultado: {ans}")
                op2 = input("Você deseja subtrair mais um número do resultado?\n1- Sim\n2- Não\nResposta: ")
#função de multiplicação
def multiplicação():
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
        ans *= float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o segundo número: ")
        if is_number(num):
            ans *= float(num)
        else:
            print("caractere inválido")

    print(f"Resultado: {ans}")
    op2 = input("Você deseja multiplicar o resultado por mais um número?\n1- Sim\n2- Não\nResposta: ")

    while(op2 != '2'):
        if(op2 == '1'):
            num = input("Digite o número que você deseja multiplicar pelo resultado: ")
            if(is_number(num)):
                ans += float(num)
                print(f"Resultado: {ans}")
                op2 = input("Você deseja multiplicar o resultado por mais um número?\n1- Sim\n2-Não\nResposta: ")
            else:
                print("Caractere inválido")
                os.system("pause")
        else:
            print("Caractere inválido")
            os.system("pause")
            os.system("cls")
            print(f"Resultado: {ans}")
            op2 = input("Você deseja multiplicar o resultado por mais um número?\n1- Sim\n2- Não\nResposta: ")
#função de divisão
def divisão():
    ans = 0
    num = input("Digite o primeiro número (Dividendo): ")
    if is_number(num):
        ans += float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o primeiro número (Dividendo): ")
        if is_number(num):
            ans += float(num)
        else:
            print("caractere inválido")

    num = input("Digite o número que irá dividir o anterior (Divisor): ")
    if is_number(num):
        ans /= float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o número que irá dividir o anterior (Divisor): ")
        if is_number(num):
            ans /= float(num)
        else:
            print("caractere inválido")

    print(f"Resultado: {ans}")
    op2 = input("Você deseja dividir o resultado por mais um número?\n1- Sim\n2- Não\nResposta: ")

    while(op2 != '2'):
        if(op2 == '1'):
            num = input("Digite o número que você deseja dividir o resultado: ")
            if(is_number(num)):
                ans /= float(num)
                print(f"Resultado: {ans}")
                op2 = input("Você deseja dividir o resultado por mais um número?\n1- Sim\n2-Não\nResposta: ")
            else:
                print("Caractere inválido")
                os.system("pause")
        else:
            print("Caractere inválido")
            os.system("pause")
            os.system("cls")
            print(f"Resultado: {ans}")
            op2 = input("Você deseja dividir o resultado por mais um número?\n1- Sim\n2- Não\nResposta: ")
#função de potenciação
def potência():
    #declaração da resposta base
    ans = 0
    num = input("Digite o primeiro número (Base): ")
    if is_number(num):
        ans += float(num)
    else:
        print("caractere inválido")
    #Laço de repetição para caso o número não seja válido, repete até ser
    while(is_number(num) == False):
        num = input("Digite o primeiro número (Base): ")
        if is_number(num):
            ans += float(num)
        else:
            print("caractere inválido")

    num = input("Digite o número que será o expoente do anterior: ")
    if is_number(num):
        ans **= float(num)
    else:
        print("caractere inválido")

    while(is_number(num) == False):
        num = input("Digite o número que será o expoente do anterior: ")
        if is_number(num):
            ans **= float(num)
        else:
            print("caractere inválido")

    print(f"Resultado: {ans}")
    op2 = input("Você deseja adicionar mais uma potência ao resultado?\n1- Sim\n2- Não\nResposta: ")
    #laço de repetição para adição dos valores consecutivos
    while(op2 != '2'):
        if(op2 == '1'):
            num = input("Digite o número que você deseja ser o expoente do resultado: ")
            if(is_number(num)):
                ans **= float(num)
                print(f"Resultado: {ans}")
                op2 = input("Você deseja adicionar mais uma potência ao resultado?\n1- Sim\n2-Não\nResposta: ")
            else:
                print("Caractere inválido")
                os.system("pause")
        else:
            print("Caractere inválido")
            os.system("pause")
            os.system("cls")
            print(f"Resultado: {ans}")
            op2 = input("Você deseja adicionar mais uma potência ao resultado?\n1- Sim\n2- Não\nResposta: ")

#Função Principal
def calculadora():
    #'menu' onde o usuário pode escolher o que deseja
    op = input("Qual operação você deseja realizar?\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potenciação\n6- Sair\nResposta: ")
    #'switch' para as opções do usuário com chamada das respectivas funções
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
    #laço para que haja uma repetição caso o usuário não escolha sair
    while(op != 6):
        op = input("Qual operação você deseja realizar?\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potênciação\n6- Sair\nresposta: ")
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
#chamada da função principal
calculadora()

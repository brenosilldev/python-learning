"""
    Conceitos básicos de Python

    variavel
"""
valores = []

# nome  = str(input("Digite seu nome: "))

# print(f"Olá {nome}, seja bem-vindo(a) ao nosso aplicativo de tarefas!")


print("Digite um número para ver a mensagem correspondente (digite 0 para sair):")
print("    1 - Adicionar números à lista .")
print("    2 - Exibir números da lista.")
print("    3 - Remover números da lista.")
print("    0 - Encerrar o programa.")

numero = None
while numero != 0:
    numero = int(input("Digite um número: "))

    if numero == 0:
        print("Você digitou 0. Encerrando o programa.")
        break

    elif numero == 1:
        print("Digite quantos numeros que adicionar na lista: ")

        qtd = int(input())

        for i in range(qtd):

            valor = int(input(f"Digite o {i+1}º número: "))
    
            valores.append(valor)
        
    elif numero == 2:
        print("Os números na lista são:")

        if len(valores) == 0:
            print("A lista está vazia.")

        print(valores)

    elif numero == 3:
        if len(valores) == 0:
            print("A lista está vazia. Não há números para remover.")
            continue
         
        print("Digite o número que deseja remover da lista: ")
        numero_a_remover = int(input())
        if numero_a_remover in valores:
            valores.remove(numero_a_remover)
            print(f"O número {numero_a_remover} foi removido da lista.")
        else:
            print(f"O número {numero_a_remover} não está na lista.")

    else:
        print("Número inválido. Tente novamente.")

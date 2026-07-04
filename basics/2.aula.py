

# while input != 0:
#     input = int(input("Digite um número: "))

#     if input == 1:
#         print("Ola")
    
#     elif input == 0:
#         print("Você digitou 0. Encerrando o programa.")
#         break

todos = []
for i , x in enumerate(range(1,21,1)):

    if x % 2 == 0:
        todos.append(x)
    print(f"i: {i} - x: {x}")


print(f"Todos os números pares de 1 a 20: {todos}")
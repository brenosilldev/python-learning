

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
        print(f"i: {i} - x: {str(x).capitalize()}")

for i in range(1,21):
    print(f"{i} - x: {str(i).capitalize()}")


print(f"Todos os números pares de 1 a 20: {todos}")



nome = str(input("Digite um nome para sair: "))
while True:
    print(nome.capitalize().title())
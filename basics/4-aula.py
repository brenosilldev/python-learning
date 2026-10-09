# Listas


# todos = []
# while True:
#     user_input = input("Digite algo: Add,Show,Edit,Delete,Exit: ")
#     user_input = user_input.strip().lower()

#     match user_input:
#         case "add":
#             item = input("Digite o item que deseja adicionar: ")
#             todos.append(item)
#             print(f"Item '{item}' adicionado com sucesso!")
#         case "show":
#             if len(todos) == 0:
#                 print("A lista está vazia.")
#             else:
#                 print("Lista de itens:")
#                 for index, item in enumerate(todos, start=1):
#                     print(f"{index}. {item}")
#         case "edit":
#             if len(todos) == 0:
#                 print("A lista está vazia. Não há itens para editar.")
#             else:
#                 print("Lista de itens:")
#                 print(todos)
#                 print('------------')
#                 item_index = int(input("Digite o número do item que deseja editar: "))

#                 number = item_index - 1

#                 if 0 <= number < len(todos):
#                     new_item = input("Digite o novo item: ")
#                     todos[number] = new_item
#                     print(f"Item '{new_item}' editado com sucesso!")
#                 else:
#                     print("Número de item inválido.")

#         case "exit":
#             print("Saindo do programa...")
#             break


# listas sao mutáveis, ou seja, podem ser alteradas após a sua criação. Já as tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.
filenames = ["1.document.txt.teste.teste.stes", "2.image.png.", "3.script.py", "4.data.csv", "5.presentation.pptx", "6.audio.mp3", "7.video.mp4", "8.archive.zip", "9.spreadsheet.xlsx", "10.webpage.html"]

for index, filename in enumerate(filenames):
    filenames[index] = filename.replace(".", "_",1) # exemplo de uso do replace() para substituir os pontos por underline, limitando a 3 substituições
    print(f"Arquivo '{filename}' renomeado para '{filenames[index]}'")


# tuplas sao imutáveis, ou seja, não podem ser alteradas após a sua criação.
filenames  = ("1.document.txt.teste.teste.stes", "2.image.png.", "3.script.py", "4.data.csv", "5.presentation.pptx", "6.audio.mp3", "7.video.mp4", "8.archive.zip", "9.spreadsheet.xlsx", "10.webpage.html")


color_codes = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(color_codes)  # Acessando o elemento 2 da primeira tupla
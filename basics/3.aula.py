# while True:
#     print(input("Digite algo: "))

#     if input("Deseja continuar? (s/n): ").lower() != 's':
#         break   

#     elif input("Deseja sair? (s/n): ").lower() == 's':
#         break


# nomes  = ['João', 'Maria', 'José', 'Ana', 'Pedro']

# for nome in nomes:
#     print(nome.capitalize())


# while len(nomes) > 0:
#     nomes.sort()
#     print(nomes)


#     match input("Deseja continuar? (s/n): ").lower():
#         case 's':
#             continue
#         case 'n':
#             break 


country = "USA" 


match country:
    case "USA" | "United States":
        print("Hello")
    case "Italy" | "Italia":
        print("Ciao")
    case "Germany" | "Deutschland":
        print("Hallo")

        employees = ["john smith", "sarah bremen", "dora dawson"]

employees = ["john smith", "sarah bremen", "dora dawson"]


for nome in employees:
    print(nome.title().capitalize().replace(" ", " - "))
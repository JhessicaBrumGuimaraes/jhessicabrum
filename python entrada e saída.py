# exempl.py

print("Olá", "Mundo", sep="-")

print("Olá", "Mundo", end="!\n")

print("18", "04", "2023",sep="/")

print("nome", "sobrenome", "email", sep=";")


nome = input("Digite seu nome: ")
print ("oi,", nome)

 #Convertendo a entrada para inteiro
idade=int(input("Digite sua dade:"))
print("Daqui cinco anos, você terá", idade + 5, "anos.")

 #Convertendo a entrada para float
altura = float(input("Digite sua altura em metros: "))
prnt("Sua altura é", atura, "metros.")

def captura_loop():
    print("Digite números para adicionar à lista (digite 'done' para terminar):")

    numeros = []

    while True:
        entrada = input()

        if entrada.lower() == 'done':
            break
        else:
            numeros.append(int(entrada))

            

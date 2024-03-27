def soma(a, b) :
    return a + b

def quadrado(a):
    return a**2

def hipotenusa(cateto1,cateto2):
    return soma(quadrado(cateto1),quadrado(cateto2))**(1/2)

def simples(cor):
    if cor == "azul":
        return "escolheu certo"
def medio(cor):
    if cor == "roxo":
        return "escolheu certo"
    else:
        return "tente outra cor"

def completo(cor):
    if cor == "rosa":
        return "escolheu certo"
    elif cor == "rosa":
        return "não tem salvação!"
    else:
        return "tente outra cor"
    
numeros = [1, 2, 3, 4, 5]
print(numeros[0])
print(numeros[-1])
numeros[0] = 10
print(numeros)

#contar de 1 à 9#

contador = 0
while contador <10:
    print(contador)
    contador += 1

#contar de novo de 1 à 9#

for i in range(10):
    print(i)


for item in [1,45,78,'a',[3,5]]:
    print(item)

#meu nome
 
for letra in 'Jhéssica':
    print(letra)

#triângulo

for i in range(6):
    print((i + 1) * "*")
    

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numero, end = " ")
print("\n--------------------------------")

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
# a primeira: numero é o retorno do que a lista vai gerar 
# a segunda parte: for numero in numeros é a iteração
# e a terceira parte: if numero % 2 == 0 é a condição da iteração, essa parte é opcional
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
print("\n--------------------------------\n")

# Como elevar todos os números da lista ao quadrado
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
    print(numero, end = " ")
print("\n--------------------------------\n")

# Como elevar todos os números da lista ao quadrado
numeros_para_quadrado = [1, 30, 21, 2, 9, 65, 34]
for numero_1 in numeros_para_quadrado:
    print(numero_1**2, end = " ")

# Modificar valores
print("\n")
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

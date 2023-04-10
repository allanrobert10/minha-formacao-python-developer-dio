'''
Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar seu valores
será necessário converter o set em uma lista
'''
# set
numeros = {1, 2, 3, 2}

# convertendo em uma lista
numeros = list(numeros)

# para poder acessar
print(numeros[0])

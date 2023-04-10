'''
A forma mais comum para percorrer os dados do conjunto é utilizando o comando for
'''

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# para saber o índice do elemento
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

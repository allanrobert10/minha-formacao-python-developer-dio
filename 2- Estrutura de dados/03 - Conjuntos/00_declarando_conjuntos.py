'''
Conjuntos = set => é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos
matemáticos ou eliminar itens duplicados de um iterável.
'''
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

# perceba que o set eu não passa a ordem correta
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

# outra forma de usar o set
linguagens = {"Python" , "Java", "Python"}
print(linguagens)

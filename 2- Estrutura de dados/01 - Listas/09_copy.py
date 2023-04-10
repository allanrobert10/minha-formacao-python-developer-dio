lista = [1, "Python", [40, 30, 20]]

# o método copy retorna uma lista igual mas com instância diferente
lista2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(lista), id(lista2))

lista2[0] = 2

print(lista)
print(lista2)

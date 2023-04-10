# lista com string
lista = ["p", "y", "t", "h", "o", "n"]

# o fatiamento é feito assim: [start:stop:step] 
# step é de quanto em quanto vai pular a posição

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

'''
O extend serve para juntas duas listas duplicando objetos se existirem
'''

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

linguagens.extend(["java", "csharp", "c", "python"])

print(linguagens)

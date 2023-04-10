'''
diferente do pop você já indica qual o objeto que você quer remover 
'''

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

print("\n-----------------------------------\n")

'''
mas se tiver mais de um objeto repetido ele vai tirar o primeiro que ele encontrar
'''

linguagens = ["python", "js", "c", "java", "csharp", "c"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

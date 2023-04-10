'''
o sort serve para ordenar alfabeticamente a lista 
'''

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)

'''
o sort(reverse=true) vai pegar a lista que vou colocada em ordem e vai fazer o reverso dela
'''
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

'''
o .sort(key=lambda x: len(x) vai ordenar de forma crescente a lista 
'''
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

'''
o .sort(key=lambda x: len(x) vai ordenar de forma decrescente a lista 
'''

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

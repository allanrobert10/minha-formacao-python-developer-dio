'''
o index se limita a primeira ocorrência, ou seja, ele mostra a posição do seu objeto
que foi verificado na primeira vez, caso você repita o nome na lista e solicite nova verificação
ele mostra o índice da primeira vez que foi verificado
'''

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

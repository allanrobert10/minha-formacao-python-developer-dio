'''
o pop ele retira sempre o último objeto da lista e a cada vez que ele é utilizado
vai tirando sempre o último
'''

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens)
print(linguagens.pop())  # java
print(linguagens)
print(linguagens.pop())  # c
print(linguagens)
print(linguagens.pop()) # python
print(linguagens)

print("\n-------------------------\n")

'''
mas também podemos indicar qual a posição queremos remover
'''
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.pop(0))  # python
print(linguagens)

'''
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. 
Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em 
estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).
'''

def somar(a, b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a*2 + a*3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação é = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação é = 0
exibir_resultado(10, 10, multiplicar)  # O resultado da operação é = 50

operacao_soma = somar
print("\nO Resultado é:",operacao_soma(1,23))

operacao_subtrair = subtrair
print("\nO Resultado é:",operacao_subtrair(1,23))

operacao_multiplicar = multiplicar
print("\nOo Resultado é:",operacao_multiplicar(1,23))

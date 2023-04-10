'''
mesmo depois da função ter sido encerrada a lista foi alterada mesmo fora da função, 
pois ela é um objeto mutável.
'''

salario_1 = 2500

def salario_bonus_2(bonus_2, lista):
    global salario_1
    lista.append(2)
    salario_1 += bonus_2
    return salario_1

lista = [1]
salario_com_bonus_2 = salario_bonus_2(1000, lista) 
print(salario_com_bonus_2)
print(lista)
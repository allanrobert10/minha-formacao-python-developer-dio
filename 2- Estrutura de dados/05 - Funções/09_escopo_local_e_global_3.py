'''
Para que a lista não seja alterada fora da função
'''
salario_1 = 2500

def salario_bonus_2(bonus_2, lista):
    global salario_1

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario_1 += bonus_2
    return salario_1

lista = [1]
salario_com_bonus_2 = salario_bonus_2(1000, lista) 
print(salario_com_bonus_2)
print(lista)
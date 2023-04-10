'''
Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. 
Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. 
Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que 
está sendo manipulada no escopo local é global. Essa NÃO é uma boa prática e deve ser evitada.
'''
# é uma variável de escopo global
salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)


salario_1 = 2500

def salario_bonus_2(bonus_2):
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

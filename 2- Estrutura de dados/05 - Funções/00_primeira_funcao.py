'''
Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, 
esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e 
possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que 
estamos programando de maneira estruturada.
'''

'''
    def funcao (param1, param 2):
        total = param' *param2
        return total

Palavra reservada builtin => def
Nome da função => funcao
Parametros da função => (param1, param 2) 
Corpo da função =>  total = param' *param2
                    return total
Declaração de retorno => return
Valor retornado => total
Assinatura da função => def funcao (param1, param 2):

'''


def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# como não existe parâmetro ele não vai retornar o print
exibir_mensagem()

# como existe parâmetro é necessário informar na chamada um nome
exibir_mensagem_2(nome="Allan")

# como existe parâmetro é necessário informar na chamada um nome que pode ser direto
exibir_mensagem_2("Robert")

# neste caso o nome já foi declarado direto no parâmetro
exibir_mensagem_3()

# caso na chamada da função eu atribua um novo nome ele sobrescreve o nome existente no parâmetro
exibir_mensagem_3(nome="Chappie")



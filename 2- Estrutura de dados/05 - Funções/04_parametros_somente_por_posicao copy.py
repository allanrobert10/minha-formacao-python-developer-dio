'''
Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. 
Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, 
assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por 
posição, por posição e nome, ou por nome.

def f (positional1, positional2, /, pos_or_keyword, *, keyword1, keyword2):
'''

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

'''
é utilizado para adicionar uma chave não existente no dicionário
'''
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# como a chave já existe no dicionário ele não vai fazer a alteração
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

'''
a gente não informa a chave que ele vai remover, ele vai removendo automaticamente de baixo para cima e caso não tenha mais chave para remover
ele informa um keyerror
''' 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
resultado = contatos.popitem()
resultado = contatos.popitem()

print(resultado)



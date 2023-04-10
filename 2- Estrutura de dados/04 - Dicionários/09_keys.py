contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# retorna somente a chave do dicionário
resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

# muito útil para saber quais as chaves existentes no dicionário
novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys()) # dict_keys(['a', 1, 'b'])

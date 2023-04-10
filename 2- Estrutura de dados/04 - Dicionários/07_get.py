contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

'''
Ao usarmos o método .get, caso a chave não exista ele retorna none
'''
resultado = contatos.get("chave")  # None
print(resultado)

# se ele não achar a chave ele retorna a {}
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

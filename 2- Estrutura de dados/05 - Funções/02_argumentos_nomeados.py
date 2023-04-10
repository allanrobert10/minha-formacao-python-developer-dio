def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# posso passar sequencialmente
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# ou passando chave valor informando no parâmetro
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# os dois ** são usados para informar que está passando um dicionário para a função 
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

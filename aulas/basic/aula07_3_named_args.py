def salvar_moto(marca, modelo, ano, placa):
    print (f"Moto inserida! {marca}/{modelo}/{ano}/{placa} ")

# Argumentos Nomeados
#salvar_moto(marca="Marca1", modelo="Modelo1", ano="2024", placa="Placa1234")
# Dicionário
salvar_moto(** {"marca":"Marca1", "modelo":"Modelo1", "ano":"2024", "placa":"Placa1234"})

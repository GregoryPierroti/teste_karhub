import pandas as pd

def ajuste_json(veiculos):
    """função criada paraajustar a lista de dados vindo da API na parte complementos, transformando em uma lista estruturada"""
    for i in veiculos:
        if 'Complemento' in list(i.keys()) and i['Complemento'] is not None:
            i['Complemento'] = i['Complemento'].split("|")
            i['Complemento'] = [j.strip() for j in i['Complemento']]
    return veiculos

def montar_df_veiculos(veiculos):
    """Função criada para criar o dataframe e realizar o explode da coluna complementos, deixando a granularidade do DF de acordo com os modelos existentes"""
    df_veiculo = pd.DataFrame(veiculos)
    return df_veiculo.explode(column='Complemento')

def retorno_veiculos(df_explode):
    """Função na qual chama as duas acima e realiza o ajuste da coluna ano, para que seja uma string e não um numero"""
    df = df_explode
    df['Ano'] = df['Ano'].astype(str)
    df['Ano'] = [str(i)[:-2] if i[0].isnumeric() else i for i in list(df['Ano'])]
    return df

def df_veiculo_final(veiculos):
    lista_json = ajuste_json(veiculos)
    df_explode = montar_df_veiculos(lista_json)
    return retorno_veiculos(df_explode)
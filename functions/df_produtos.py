import pandas as pd

#Acessando o arquivo XLSX para tratar os dados em um DF
karhub_autoparts = pd.read_excel("source/karhub_autoparts_1.xlsx")

def df_pivot(karhub_autoparts):
    """Criando DF separado para valor atributo e nome atributo, para em seguida realizar o pivot"""
    df_atributos = karhub_autoparts\
    .drop("Nome SKU", axis='columns')\
    .drop("Fabricante", axis='columns')\
    .drop("Código", axis='columns')\
    .drop("Composição", axis='columns')\
    .drop("Categoria", axis='columns')
    return df_atributos.pivot(values='Valor Atributo', columns='Nome Atributo')

def dict_agg(karhub_autoparts):
    """Criando dicionario no qual é usado para que os valores dos atributos se encontrem na mesma linha de acordo com o agrupamento em questão"""
    #Lendo o DF primario e pegando todos os atributos existentes
    atributos = list(set(karhub_autoparts['Nome Atributo']))
    #Criando o dicionario e passando os atributos como chave, acompanhando o valor "first", 
    return {cont: "first" for cont in atributos}

def agg_df(autoparts,dic_atributos):
    """Agrupando o dataframe e juntando todos os valores dos atributos de uma instância na mesma linha"""
    return autoparts.groupby("Código").agg(dic_atributos).reset_index()


def ajuste_tipagem_numero_espirais(autoparts_atributo_final):
    """Removendo as vírguulas de  uma coluna e ajustando para ."""
    autoparts_atributo_final['Número de Espirais'] = autoparts_atributo_final['Número de Espirais'].astype(str)
    autoparts_atributo_final['Número de Espirais'] = autoparts_atributo_final['Número de Espirais'].str.replace(',', '.').replace('None','0')
    autoparts_atributo_final['Número de Espirais'] = autoparts_atributo_final['Número de Espirais'].astype(float)
    return autoparts_atributo_final

def inclusao_df_nomes(autoparts_atributo_final, karhub_autoparts):
    """Inserindo as colunas de Nome SKU, categoria, fabricante e composição no DF"""
    return autoparts_atributo_final.join(karhub_autoparts.drop(['Código', 'Valor Atributo', 'Nome Atributo']\
                                                                      , axis="columns"))
    
def reordenar_colunas(autoparts_final):
    """Levando as colunas de categorização dos produtos para o inicio do DF"""
    return pd.concat([autoparts_final.iloc[:, -4:], autoparts_final.iloc[:, :-4]], axis=1)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def df_produto_final():
    """Função que executa as outras na ordem adequada para tratamento"""
    df_pivot1 = df_pivot(karhub_autoparts)

    #Join necessário para segui com o tratamento, no qual o pivot ja foi feito
    autoparts = karhub_autoparts.join(df_pivot1)

    df_agg = agg_df(autoparts, dict_agg(karhub_autoparts))

    df_ajuste_pontuacao = ajuste_tipagem_numero_espirais(df_agg)

    df_inclusao_nomes = inclusao_df_nomes(df_ajuste_pontuacao, karhub_autoparts)

    return reordenar_colunas(df_inclusao_nomes)
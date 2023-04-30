def credencial_bq():
    """Função na qual le as credenciais no arquivo .py e passa para o comando no qual valida as credenciais para que possamos escrever no big query"""
    from google.oauth2.service_account import Credentials
    from source.credential import credencial
    return Credentials.from_service_account_info(info=credencial())

def write_bigquery():
    import pandas as pd
    """Função na qual estabelecemos os parametros para escrever no dataframe e ja escrevemos o mesmo dentro da tabela no big query"""
    project_id = "karhub-data-engineer-test"
    dataset_id = "cadastro_produto"
    table_id = "kh_data_engineer_teste_gregorypierroti3"
    tabela = f'{project_id}.{dataset_id}.{table_id}'
    return [tabela, project_id]
    
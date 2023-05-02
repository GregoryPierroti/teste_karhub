# Desafio Técnico - Documentação do Projeto
## Introdução
### Este projeto tem como objetivo processar dados de diferentes fontes e consolidá-los em um único dataframe para posterior análise. Ele consiste em uma série de funções e arquivos que são executados em conjunto para obter o resultado final.

## Pré-requisitos
Para executar este projeto, é necessário ter as seguintes dependências instaladas:

- Python 3.6 ou superior
- Bibliotecas Python: pandas, google-cloud-bigquery, google-auth, google-auth-oauthlib, google-auth-httplib2 e requests

## Instalação
Clone este repositório em sua máquina local.
Crie um ambiente virtual Python e ative-o.
Instale as dependências necessárias com o seguinte comando: pip install -r requirements.txt.

## Estrutura do projeto
O projeto é composto pelas seguintes pastas e arquivos:

karhub_project/
├── venv/
├── source/
│   ├── karhub_autoparts_1.xlsx
│   └── Karhub-alias.csv
├── functions/
│   ├── bigquery.py
│   ├── connect_api.py
|   ├── df_alias.py
|   ├── df_produtos.py
|   ├── df_veiculos.py
├── requirements.txt
├── README.md
├── df_final.ipynb
└── query.ipynb

- venv: ambiente virtual Python criado para armazenar os recursos de biblioteca para facilitar o funcionamento do projeto.
- source: pasta na qual se encontram os arquivos csv e xlsx que serão consumidos, além das credenciais de acesso ao Big Query que não serão incluídas no GitHub para proteger os dados.
- functions: pasta na qual se encontram os arquivos Python que auxiliam na formação do dataframe final.
1. bigquery.py: arquivo que contém a função credencial_bq() para credenciar os acessos ao Big Query com base no arquivo credential.py da pasta source, e a função write_bigquery() para estabelecer os parâmetros da tabela que será escrita no Big Query. É importante destacar que não é possível fazer replace no banco de dados com os acessos atuais, portanto é necessário mudar o nome do table_id caso seja necessário testar a escrita.
connect_api.py: arquivo que contém a função consumir_api() para fazer acesso ao token e a função gerar_dados_veiculos() para retornar os resultados utilizando o token.
2. df_alias.py: arquivo que contém a função ler_dataframe_alias() para ler um dataframe da tabela 'DE/PARA'.
3. df_veiculos.py: arquivo que contém funções que realizam os tratamentos solicitados no desafio, incluindo a função tratar_dados_veiculos() que realiza as outras funções de forma organizada.
4. df_produtos.py: arquivo que contém funções que realizam os tratamentos necessários nos dados do dataframe de produtos. A função tratar_dataframe_produtos() executa as outras funções na ordem necessária.
- df_final.ipynb: arquivo de Jupyter Notebook que centraliza e executa os módulos Python da pasta functions para trazer os dados e realizar as principais ações e ajustes finais para salvar o dataframe no Big Query.
- query.ipynb: arquivo de Jupyter Notebook que responde às perguntas realizadas no fim do desafio proposto.

## Execução
Para executar o projeto, abra o arquivo df_final.ipynb em um ambiente Jupyter Notebook e execute todas as células do arquivo. O resultado final será um dataframe consolidado que será salvo no Big Query.

## Conclusão
Este projeto teve como objetivo realizar o tratamento de dados de diferentes fontes e formatos, a fim de gerar um único dataframe com as informações relevantes para o negócio. Para isso, utilizou-se a linguagem Python e suas bibliotecas, além de acesso ao Google Cloud Platform e ao BigQuery.

Durante o processo, foram realizadas diversas etapas de transformação e limpeza de dados, envolvendo diferentes técnicas e abordagens. Também foi necessário realizar a integração de dados de diferentes fontes, como planilhas, APIs e bancos de dados, além de lidar com diferentes formatos de dados, como CSV e JSON.

Ao final, o dataframe final gerado foi salvo no BigQuery, permitindo a análise e visualização dos dados de forma eficiente. O projeto teve sucesso em seu objetivo de integrar e tratar dados de diferentes fontes, tornando-os prontos para análise e tomada de decisão.

Este projeto pode ser utilizado como base para projetos semelhantes que necessitem da integração e tratamento de dados de diferentes fontes e formatos, além de servir como um exemplo de boas práticas em análise e tratamento de dados.
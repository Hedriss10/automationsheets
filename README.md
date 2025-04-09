# Automation Spreedsheets

Automation Spreadsheet é uma solução robusta e eficiente para ETL **(Extract, Transform, Load)** que processa dados de planilhas CSV e os persiste em um banco de dados `PostgreSQL`. Desenvolvido com foco em desempenho e escalabilidade, o script utiliza `Polars` para mmanipulação de dados em memória, `SQLAlchemy` para integração com banco de dados e boas práticas de engenharia de software.

Este script foi criado para lidar com grandes volumes de dados estruturados, como informações pessoais e de contato, aplicando transformações avançadas e garantindo consistência ao carregar os dados em uma estrutura relacional gerenciada em `SQLAlchemy`.

## Etapa do processo

- 1 - Carregamento de dados 
- 2 - Tratamento de dados
- 3 - Limpeza de dados
- 4 - Exportação de para o banco de dados

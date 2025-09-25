# Persistência Poliglota com GeoProcessamento

Este projeto demonstra o uso de SQLite + MongoDB com Python e Streamlit para geoprocessamento.

## Funcionalidades

- Cadastro de cidades (SQLite)
- Cadastro de locais (MongoDB)
- Consulta de locais por cidade
- Listagem de locais próximos a uma coordenada
- Visualização em mapa

## Execução

1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Certifique-se de ter um MongoDB rodando em `localhost:27017`.
3. Execute o app:
```bash
streamlit run app.py
```
4. Acesse no navegador o link indicado pelo Streamlit.

---
Projeto desenvolvido para prática de persistência poliglota e geoprocessamento.

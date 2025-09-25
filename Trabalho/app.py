import streamlit as st
import pandas as pd
from db_sqlite import init_db, get_cidades, add_cidade_estado
from db_mongo import add_local, get_locais_by_cidade, get_locais_proximos
from geoprocessamento import calcular_distancia
import folium
from streamlit_folium import st_folium

st.title("Persistência Poliglota com GeoProcessamento")

# Inicializar banco SQLite
init_db()

menu = st.sidebar.selectbox("Menu", ["Cadastrar Cidade/Estado", "Cadastrar Local", "Consultar Locais", "Locais Próximos"])

if menu == "Cadastrar Cidade/Estado":
    st.header("Cadastro de Cidade e Estado")
    nome = st.text_input("Nome da cidade")
    estado = st.text_input("Estado")
    if st.button("Salvar"):
        add_cidade_estado(nome, estado)
        st.success("Cidade/Estado salvo com sucesso!")

elif menu == "Cadastrar Local":
    st.header("Cadastro de Local (MongoDB)")
    nome_local = st.text_input("Nome do local")
    cidade = st.text_input("Cidade")
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    descricao = st.text_area("Descrição")
    if st.button("Salvar"):
        add_local(nome_local, cidade, latitude, longitude, descricao)
        st.success("Local salvo no MongoDB!")

elif menu == "Consultar Locais":
    st.header("Consultar Locais de uma Cidade")
    cidades = [c[0] for c in get_cidades()]
    cidade_sel = st.selectbox("Selecione a cidade", cidades)
    if st.button("Buscar Locais"):
        locais = get_locais_by_cidade(cidade_sel)
        df = pd.DataFrame(locais)
        st.dataframe(df)
        if not df.empty:
            mapa = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)
            for _, row in df.iterrows():
                folium.Marker([row['latitude'], row['longitude']], popup=row['nome_local']).add_to(mapa)
            st_folium(mapa, width=700, height=500)

elif menu == "Locais Próximos":
    st.header("Locais Próximos de uma Coordenada")
    lat = st.number_input("Latitude", format="%.6f")
    lon = st.number_input("Longitude", format="%.6f")
    raio = st.number_input("Raio em km", value=10.0)
    if st.button("Buscar"):
        locais = get_locais_proximos(lat, lon, raio)
        df = pd.DataFrame(locais)
        st.dataframe(df)
        if not df.empty:
            mapa = folium.Map(location=[lat, lon], zoom_start=12)
            folium.Marker([lat, lon], popup="Você está aqui", icon=folium.Icon(color="red")).add_to(mapa)
            for _, row in df.iterrows():
                folium.Marker([row['latitude'], row['longitude']], popup=row['nome_local']).add_to(mapa)
            st_folium(mapa, width=700, height=500)

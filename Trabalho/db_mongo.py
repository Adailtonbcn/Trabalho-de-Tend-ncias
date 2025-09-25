from pymongo import MongoClient
from geoprocessamento import calcular_distancia

client = MongoClient("mongodb://localhost:27017/")
db = client["geodados"]
collection = db["locais"]

def add_local(nome_local, cidade, latitude, longitude, descricao):
    doc = {
        "nome_local": nome_local,
        "cidade": cidade,
        "coordenadas": {"latitude": latitude, "longitude": longitude},
        "descricao": descricao
    }
    collection.insert_one(doc)

def get_locais_by_cidade(cidade):
    locais = collection.find({"cidade": cidade})
    return [{"nome_local": l["nome_local"],
             "cidade": l["cidade"],
             "latitude": l["coordenadas"]["latitude"],
             "longitude": l["coordenadas"]["longitude"],
             "descricao": l["descricao"]} for l in locais]

def get_locais_proximos(lat, lon, raio_km):
    locais = collection.find()
    proximos = []
    for l in locais:
        lat2 = l["coordenadas"]["latitude"]
        lon2 = l["coordenadas"]["longitude"]
        dist = calcular_distancia(lat, lon, lat2, lon2)
        if dist <= raio_km:
            proximos.append({
                "nome_local": l["nome_local"],
                "cidade": l["cidade"],
                "latitude": lat2,
                "longitude": lon2,
                "descricao": l["descricao"],
                "distancia_km": round(dist, 2)
            })
    return proximos

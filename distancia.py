import requests

API_KEY = "f6d7dd27-aa75-457a-8d25-e0fc01af9d91"

def obtener_coordenadas(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }

    respuesta = requests.get(url, params=params)
    if respuesta.status_code == 200 and respuesta.json()["hits"]:
        coord = respuesta.json()["hits"][0]
        return f"{coord['point']['lat']},{coord['point']['lng']}"
    else:
        print(f"❌ No se pudo obtener coordenadas para: {ciudad}")
        return None

def obtener_direccion(origen_coord, destino_coord, transporte):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [origen_coord, destino_coord],
        "vehicle": transporte,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        path = data["paths"][0]
        distancia_km = path["distance"] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_seg = path["time"] / 1000
        instrucciones = path["instructions"]

        print(f"\n📍 Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
        print(f"⏱️ Tiempo estimado: {duracion_seg / 60:.2f} minutos")
        print("\n🗺️ Narrativa del viaje:")
        for paso in instrucciones:
            print(f" → {paso['text']}")
        print()
    else:
        print("❌ Error al calcular la ruta. Revisa el transporte o las coordenadas.")

# Bucle principal
while True:
    print("=== CALCULADORA DE DISTANCIA ===")
    origen = input("Ciudad de origen (o 's' para salir): ")
    if origen.lower() == "s":
        break
    destino = input("Ciudad de destino: ")
    transporte = input("Tipo de transporte (car, foot, bike): ")

    origen_coord = obtener_coordenadas(origen)
    destino_coord = obtener_coordenadas(destino)

    if origen_coord and destino_coord:
        obtener_direccion(origen_coord, destino_coord, transporte)


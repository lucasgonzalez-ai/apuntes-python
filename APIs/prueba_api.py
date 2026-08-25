import requests

# 1. Apuntamos al endpoint específico de artistas
url = 'https://musicbrainz.org/ws/2/artist'

# 2. Usamos "query" para la búsqueda y pedimos formato "json" ya que por defecto esta en XML en esta api
query_params = {
    "query": "Dream Theater",
    "fmt": "json"
}

response = requests.get(url, params=query_params)

# 3. Convertimos la respuesta en un diccionario de Python
datos = response.json()

# ¡Ahora sí puedes manipular la información!
# Entramos a la lista de 'artists', tomamos el primero (índice 0) y extraemos datos
primer_resultado = datos['artists'][0]

print(f"Banda encontrada: {primer_resultado['name']}")
print(f"Lugar de origen: {primer_resultado['area']['name']}")
print(f"Año de formación: {primer_resultado['life-span']['begin']}")
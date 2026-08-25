import requests

url = 'https://musicbrainz.org/ws/2/artist'

print("--- Ejemplo 1: Averiguar el tipo de contenido (Content-Type) ---")
# Hacemos la petición pidiendo explícitamente JSON en los parámetros
parametros_1 = {"query": "Dream Theater", "fmt": "json"}
response_1 = requests.get(url, params=parametros_1)

# Imprimimos la cabecera content-type de la respuesta
print("Content-Type de la respuesta:", response_1.headers["content-type"])


print("\n--- Ejemplo 2: Averiguar la cabecera 'accept' de la respuesta ---")
response_2 = requests.get(url, params=parametros_1)

# Usamos .get() en lugar de [] para evitar que el programa falle si la cabecera no existe.
# Como 'accept' es normalmente una cabecera de petición, el servidor de MusicBrainz no la devuelve.
cabecera_accept = response_2.headers.get("accept", "El servidor no devolvió la cabecera 'accept'.")
print("Cabecera accept (Respuesta):", cabecera_accept)


print("\n--- Ejemplo 3: Enviar cabecera 'accept' en la petición para recibir JSON ---")
# MusicBrainz es una API muy bien diseñada. Si no le pasamos "fmt": "json" en los parámetros, 
# podemos pedírselo formalmente a través de las cabeceras de nuestra solicitud.

parametros_3 = {"query": "Dream Theater"} # Ya no usamos fmt=json aquí

# Configuramos nuestra cabecera para exigir un JSON
cabeceras_peticion = {'accept': 'application/json'}

# Hacemos la petición enviando tanto los parámetros como las cabeceras
response_3 = requests.get(url, params=parametros_3, headers=cabeceras_peticion)

# Imprimimos los primeros 500 caracteres del texto para confirmar que nos devolvió un JSON 
# (lo recorto para que no te inunde la terminal con texto gigante, esto tarda un poco en procesarse)
print("Texto de la respuesta (primeros 500 caracteres):")
print(response_3.text[:300] + "\n... [Texto recortado]")
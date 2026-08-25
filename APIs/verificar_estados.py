import requests

# Parámetros básicos para que MusicBrainz nos devuelva JSON si la ruta existe
parametros = {
    "query": "Dream Theater",
    "fmt": "json"
}

print("--- Ejemplo 1: Petición exitosa ---")
# Usamos la ruta correcta: /artist
response_1 = requests.get('https://musicbrainz.org/ws/2/artist', params=parametros)

if response_1.status_code == 200:
    print('¡El servidor respondió exitosamente!')


print("\n--- Ejemplo 2: Ruta inexistente (con números) ---")
# Forzamos un error pidiendo una ruta que no existe en MusicBrainz: /peliculas
response_2 = requests.get('https://musicbrainz.org/ws/2/peliculas', params=parametros)

if response_2.status_code == 200:
    print('¡El servidor respondió exitosamente!')
elif response_2.status_code == 404:
    print('¡Ups, esa ruta en la API no pudo ser encontrada! (Error 404)')


print("\n--- Ejemplo 3: Ruta inexistente (con requests.codes) ---")
# Repetimos la petición a la ruta falsa para probar la otra sintaxis
response_3 = requests.get('https://musicbrainz.org/ws/2/peliculas', params=parametros)

if response_3.status_code == requests.codes.ok:
    print('¡El servidor respondió exitosamente!')
elif response_3.status_code == requests.codes.not_found:
    print('¡Ups, esa ruta en la API no pudo ser encontrada usando requests.codes!')
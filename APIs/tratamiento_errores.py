import requests

url = 'https://musicbrainz.org/ws/2/artist'
parametros = {"query": "Dream Theater"}

print("--- Prueba 1: Pidiendo XML (Formato soportado) ---")
headers_xml = {'accept': 'application/xml'}
response_xml = requests.get(url, params=parametros, headers=headers_xml)

if response_xml.status_code == 406:
    print('El servidor no puede responder en XML')
    # Usamos .get() por si el servidor no incluye la cabecera 'accept' en el error
    print('Tipos aceptados: ' + response_xml.headers.get('accept', 'No especificados'))
else:
    print('¡Éxito! Como esperábamos, MusicBrainz sí soporta XML.')
    # Recorto el texto a 200 caracteres para no llenar tu terminal
    print(response_xml.text[:200] + "\n... [Texto XML recortado]\n")


print("--- Prueba 2: Forzando un error con un formato no soportado (PDF) ---")
headers_pdf = {'accept': 'application/pdf'}
response_pdf = requests.get(url, params=parametros, headers=headers_pdf)

# En el mundo real, algunas APIs usan el error 406 (Not Acceptable) para formatos inválidos, 
# pero otras usan 400 (Bad Request). Atraparemos ambos para estar seguros.
if response_pdf.status_code == 406 or response_pdf.status_code == 400:
    print(f'Fallo detectado (Código {response_pdf.status_code}): El servidor no aceptó responder con un PDF.')
    
    # Comprobamos si el servidor nos dice qué formatos acepta en caso de error
    tipos_aceptados = response_pdf.headers.get('accept', 'El servidor no especificó tipos válidos en su cabecera de error.')
    print('Tipos aceptados: ' + tipos_aceptados)
else:
    print('Petición exitosa. (Curioso: la API ignoró nuestra cabecera PDF y respondió de todos modos).')
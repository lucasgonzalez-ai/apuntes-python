'''
Una tabla de datos no es más que una LISTA de DICCIONARIOS. Cada diccionario es una fila. Cada clave es una columna. 
Cuando uses Pandas, por debajo es exactamente esto — pero con superpoderes. Primero domina la versión pura.
'''

# Una "tabla" de ventas como lista de diccionarios
ventas = [
    {"fecha": "2024-01-15", "producto": "Laptop", "importe": 1299.00},
    {"fecha": "2024-01-15", "producto": "Monitor", "importe": 349.99},
    {"fecha": "2024-01-16", "producto": "Teclado", "importe": 79.99},
    {"fecha": "2024-01-16", "producto": "Laptop", "importe": 1299.00},
    {"fecha": "2024-01-17", "producto": "Ratón", "importe": 29.99},
]

# Filtrar: ventas de más de 100€
grandes = [v for v in ventas if v["importe"] > 100]
print(f"Ventas grandes: {len(grandes)}")

# Transformar: extraer solo importes
importes = [v["importe"] for v in ventas]
print(f"Total facturado: {sum(importes):.2f}€")

# Agrupar: ventas por producto
from collections import Counter
productos_vendidos = [v["producto"] for v in ventas]
conteo = Counter(productos_vendidos)
print(f"Ventas por producto: {dict(conteo)}")


#EXPLICACION DETALLADA
'''
- ventas = [{...}, {...}, ...] → lista de diccionarios. Cada diccionario es una "fila" con las mismas claves.
- [v for v in ventas if v["importe"] > 100] → filtra registros por condición (como WHERE importe > 100 en SQL).
- [v["importe"] for v in ventas] → extrae un solo campo de cada registro (como SELECT importe).
- Counter(lista) → cuenta cuántas veces aparece cada elemento (como GROUP BY + COUNT).

Esta estructura lista-de-diccionarios es EXACTAMENTE lo que Pandas llama DataFrame y lo que obtienes 
al leer un JSON de una API. Dominarla aquí te prepara para Pandas sin salto conceptual.
'''
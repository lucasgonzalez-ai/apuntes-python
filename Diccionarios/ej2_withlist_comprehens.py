productos = [
    {"nombre": "Laptop", "categoria": "electrónica", "precio": 1299},
    {"nombre": "Camiseta", "categoria": "ropa", "precio": 25},
    {"nombre": "Monitor", "categoria": "electrónica", "precio": 399},
    {"nombre": "Pantalón", "categoria": "ropa", "precio": 55},
    {"nombre": "Teclado", "categoria": "electrónica", "precio": 89},
    {"nombre": "Zapatos", "categoria": "ropa", "precio": 120},
]

por_categoria = {}
for producto in productos:
    cat = producto["categoria"]
    if cat not in por_categoria:
        por_categoria[cat] = []
    por_categoria[cat].append(producto)

for cat, prods in por_categoria.items():
    nombres = [p["nombre"] for p in prods]
    print(f"{cat}: {nombres}")


'''
Patrón de agrupamiento manual: un diccionario donde cada clave es un grupo y el valor es una lista. Es exactamente lo que 
hace GROUP BY en SQL.

"if cat not in por_categoria" crea la lista vacía la primera vez que aparece una categoría. Sin eso, .append() lanzaría KeyError.

Una alternativa más pythónica sería defaultdict(list) de collections, pero entender la versión manual primero es fundamental.

Error común: reasignar por_categoria[cat] = [producto] en vez de append — eso machaca los anteriores y deja 
una sola entrada por categoría.
'''    
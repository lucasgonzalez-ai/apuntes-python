ventas_mes = [
    {"cliente": "Ana", "importe": 320.00},
    {"cliente": "Luis", "importe": 890.50},
    {"cliente": "María", "importe": 150.00},
    {"cliente": "Pedro", "importe": 1200.00},
    {"cliente": "Sara", "importe": 45.99},
    {"cliente": "Jorge", "importe": 670.00},
]

ventas_vip = [v for v in ventas_mes if v["importe"] > 500]
total_vip = sum([v["importe"] for v in ventas_vip])

print("Clientes VIP (>500€):")
for venta in ventas_vip:
    print(f"  {venta['cliente']}: {venta['importe']:.2f}€")
print("")
print(f"Total VIP: {total_vip:.2f}€")


#List comprehension con condición: [v for v in lista if condición]. Crea una nueva lista solo con los elementos que cumplen 
# el filtro — es el WHERE de SQL.

#sum([v["importe"] for v in ventas_vip]) suma un campo de cada diccionario. La versión con corchetes (lista) funciona igual 
# que sin ellos (generator), y es la que ya has visto en esta lección.

#El patrón filtrar → calcular → mostrar es el ABC del análisis de datos.
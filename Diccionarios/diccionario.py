# Colecciones de pares clave valor, ordenados

auto = {
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}    

print(auto)

# 2 formas de obtener un valor
print(auto["marca"])
print(auto.get("marca"))

# Para obtener la key o clave, o valores values por separado
print(auto.keys())
print(auto.values())

print("-------------------------")
if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")

#Reemplazo de valores
auto["año"] = 2020
print(auto)

#Agregar propiedad
auto["color"] = "Verde"
print(auto)

auto.update({"año": 2022, "puertas": 4})
print(auto)

print("------OTRO DICCIONARIO--------")
products_dict = {"AGB32": 10, "HVT": 17,
                 "TUX": 55, "FKU": 94}

print(products_dict)

# Para ver el diccionario completo ademas de imprimir se usa .items
# .items es util cuando se realiza iteraciones sobre una variable
# Esto nos devuelve como una tupla
print(products_dict.items())

# Eliminar elementos

# auto.pop("puertas")
# print(auto)

# auto.popitem()   esto elimina el ultimo elemento del diccionario
# print(auto)

# auto.clear()   Vaciar el diccionario
# print(auto)

for k in auto: # keys
    print(k)

print("----3 tipos de bucles para recorrer diccionarios----")
for v in auto.values(): # values
    print(v)

for k,v in auto.items(): # keys, value
    print(k,v)

# Diccionarios Anidados

familia = {
    "hijo1" : {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2" : {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3" : {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print(familia["hijo1"]["nombre"])
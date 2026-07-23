numerology = [55, 66, 12, 3, 87, 34, 99, 28]
ordenados = sorted(numerology)
print(ordenados)

print("----- -----  ----- -----")
# Ordenar en forma Descendente
numerology = [55, 66, 12, 3, 87, 34, 99, 28]
ordenados_desc = sorted(numerology, reverse=True)
print(ordenados_desc)


#Contar cuantas veces se repite un elemento en una lista
language = ["python", "Java", "Kotlin", "Julia", "C++", "SQL", "Java"]
print(language.count("Java"))


print("----- -----  ----- -----")
#MUY IMPORTANTE PARA LIMPIEZA DE DATOS DATA CLEANING
#separar en una lista y si el separador es punto ponerlo como "."

e2   = 'grecia_diego_celeste_kevin_gaby_guillermo'
e2_x = e2.split("_")

print(e2_x)
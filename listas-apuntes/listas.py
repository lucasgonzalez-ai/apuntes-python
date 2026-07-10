# Las listas son ordenadas, modificables y permiten valores duplicados

# Indices:  0        1           2          3
perro = ["dogo", "doberman", "pitbull", "caniche", "pastor belga"]

print(perro)

print(perro[1])

#Hacer un cambio de elemento

perro[3] = "collie"
print(perro)

#Se puede combinar elementos de diferente tipo
lista = ["Lucas", 6, True]
print(lista)
print(len(lista))

print(perro[0:2])

# Desde el uno hasta el final
print(perro[1:])


if "pastor belga" in perro:
    print("El pastor belga si esta en la lista")
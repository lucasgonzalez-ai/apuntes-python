motos = ["zanella", "kawasaki", "yamaha", "honda", "benelli", "BMW"]

#Append agrega un elemento al final de la lista

motos.append("suzuki")
print(motos)

# Insert para agregar un elemento en una posicion especfica

motos.insert(1, "ktm")
print(motos)

# Remove para eliminar un elemento

motos.remove("kawasaki")
print(motos)

#POP para eliminar por indice
motos.pop(5)
print(motos)    #['zanella', 'ktm', 'yamaha', 'honda', 'benelli', 'suzuki']

# Sort Para ordenar 
motos.sort()
print(motos)

# Reverse  ordenar de mayor a menor
motos.reverse()
print(motos)

# Unir colecciones 2 formas

coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

coleccion3 = [9, 8, 7, 6, 5]

coleccion4 = coleccion1 + coleccion2
print(coleccion3)


coleccion1.extend(coleccion3)
print(coleccion1)
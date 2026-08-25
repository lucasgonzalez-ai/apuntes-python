# SLICING - REPLACE & SPLIT

# Extraer una letra por indice
texto = "Dream Theater 2026"

print(texto[3])

# Slicing (tomar una parte del texto)
print(texto[0:5])

print(texto[:5])

print(texto[6:])

print(texto[6:-2])

#Reemplazar una palabra REPLACE, reemplaza todas las veces que aparezca la palabra

curso = "este es un curso de git"
print(curso.replace("git", "platzi")) 

#SPLIT dividir palabras y convertirlo en lista
john_petrucci = "play at movistar arena bsas"

guitarra = john_petrucci.split(" ") 
print(guitarra)

# Normalizacion
texto2 = "INTELIGENCIA artificial es una ciencia"
print("inteligencia" in texto2)

print("inteligencia".lower() in texto2.lower())
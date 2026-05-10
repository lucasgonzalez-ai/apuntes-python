# Cuantos caracteres tiene una palabra?
palabra = "Murcielago"

print(len(palabra))

#Buscar una palabra (esto es case sensitive)
texto = "Este Curso es de Fundamentos de Python"

estaIncluida = "Python" in texto
noestaIncluida = "Javascript" not in texto

print(estaIncluida)
print(noestaIncluida)

#Convertir texto a Mayusculas y/o minuscula

mayuscula = texto.upper()
print(mayuscula)

minuscula = texto.lower()
print(minuscula)

#Quitar espacios del principio o final
espacios = "    Este es el Texto"

sinEspacios = espacios.strip()

print(sinEspacios)

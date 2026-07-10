# Creando una lista de reproducción para la fiesta

# Create the playlist variable
playlist = [1, 'Blinding Lights', 'The Weeknd', 2, 'One Dance', 'Drake', 3, 'Uptown Funk', 'Mark Ronson', 4, 'Closer', 'The Chainsmokers', 5, 'One Kiss', 'Calvin Harris', 6, 'Mr. Brightside', 'The Killers']

# Print the list
print(playlist)

# Busca el nombre de la segunda canción, que es el quinto elemento en playlist e imprime el valor.
# Imprime el nombre del artista de la última canción en playlist.
# Imprime el Nombre de cada canción en playlist. (Slicing de listas)

print(playlist[4])
print(playlist[-1])
print(playlist[1::3])


##TIP PARA LISTAS
# -1 es el ultimo valor, y un rango se solicita con el indice del primer valor separado con : del indice del segundo +1. 
# O pensarlo como que el indice va solo en el primer valor y en el segundo solo el orden.
# Ejemplo: 1:3

# Si queremos traer desde un rango hasta el final simplemente ponemos prices [3:]
# Y si queremos desde el principio hasta tal elemento ponemos alreves [:3]
# Para capturar cada segundo elemento es decir, de 2 en 2 por ejemplo usamos doble dos puntos asi [::2]
# Para empezar desde el segundo valor de la lista y obtener cada tercer valor ponemos [1::3]

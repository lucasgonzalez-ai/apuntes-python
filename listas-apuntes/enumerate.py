# Lista con las frecuencias cardíacas registradas del paciente A.
# Cada elemento representa una medición realizada en un momento distinto.
frecuencia_paciente_A = [77, 82, 75, 80, 79, 78]

# Lista vacía donde se almacenarán únicamente las frecuencias mayores a 80.
registros_altos = []

# enumerate() recorre la lista y devuelve dos valores en cada vuelta:
# i -> posición (índice) del elemento, comenzando desde 0.
# frecuencia -> valor almacenado en esa posición.
for i, frecuencia in enumerate(frecuencia_paciente_A):

    # Comprueba si la frecuencia cardíaca es mayor que 80.
    if frecuencia > 80:

        # Si cumple la condición, agrega ese valor a la lista registros_altos.
        registros_altos.append(frecuencia)

        # Muestra un mensaje indicando en qué registro (índice)
        # se encontró una frecuencia superior a 80.
        print(f"¡Alerta en el registro {i}! Valor: {frecuencia}")

# Al finalizar el recorrido, muestra la lista con todas
# las frecuencias que superaron el valor de 80.
print(registros_altos)


    

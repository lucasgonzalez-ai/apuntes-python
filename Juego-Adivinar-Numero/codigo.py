import random  # importamos el modulo random para generar numeros aleatorios

nombre = "Estudiante"  # declaramos un string que identifica a la persona que adivinara el numero
intentos = 3         # declaramos la cantidad de intentos
pista = True        # declaramos un booleano

numero_secreto = random.randint(1, 10) # llama al modulo importado y con la funcion randit genera un numero entero aleatorio entre 1 y 10 y la guarda en esta variable.
                                      # Este sera el numero que se debe adivinar

print(f"Hola {nombre}, intenta adivinar el número secreto entre 1 y 10.")  # Imprime por pantalla un saludo y describe lo que debe hacer
print(f"Tienes {intentos} intentos.")  # Imprime en pantalla la cantidad de intentos que tiene el usuario


for i in range(intentos): # repite el proceso 3 veces a menos que se adivine antes
    intento = int(input("Ingresa tu número: ")) # Pide al usuario que ingrese un numero entero que se guarda en la variable intento

    if intento == numero_secreto:  # Compara si el numero ingresado por el usuario es igual al numero secreto generado por randit
        print("¡Felicitaciones! Adivinaste el número secreto 🎉") # Imprime las felicitaciones al ganar
        break  # Si la condicion de este bloque se cumple rompe el bucle y sale del mismo
    else:   # entonces
        print("No es correcto.")  # Imprime por pantalla No es Correcto, haciendo referencia al numero ingresado

        if pista:  # Pista es verdadero y siempre entra al bloque if para que haya pistas
            if intento < numero_secreto:  #Compara si la cantidad de intentos es menor al numero secreto
                print("Pista: el número secreto es mayor.")  # Devuelve el mensaje que el numero es mayor
            else:   # Sino
                print("Pista: el número secreto es menor.")  # Devuelve el mensaje que el numero es menor
else:    # Pertenece al bloque for por lo que se ejecuta solo si no sucede el break, es decir si el usuario adivino el numero
    print(f"Lo siento, se acabaron los intentos. El número secreto era {numero_secreto}.")  # En caso de que el usuario no haya acertado el numero secreto
                    #  Devuelve este mensaje y muestra el numero secreto que se genero de manera aleatoria


'''
El programa elige un numero del 1 al 10 de manera aleatoria y el usuario tiene 3 intentos para adivinarlo.
Si fallas, te dice si es mayor o menor como pista, y te quedan 2 intentos. Cuando aciertas ganas, sino pierdes, se acaba el juego
y te dice el numero secreto.
'''
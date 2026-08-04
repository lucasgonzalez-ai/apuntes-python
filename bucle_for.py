# El bucle FOR en Python es elegante: "para cada cosa en esta colección, haz algo con esa cosa".

palabra = "aprender"

#letra sera la variable iterado generalmente i

# for letra in palabra:
#     print(letra)


# una vez que entra al bucle repite con el primer elemento del primer bucle
# los n elementos del segundo bucle
adjetivos = ["oscuro", "rapido"]
metal = ["black", "thrash", "power", "heavy"]

for adjetivo in adjetivos:
    for genero in metal:
        print(adjetivo, genero)





# for genero in metal:
#      print(genero)
# else: 
#      print("ya no hay elementos en la lista")

print("------------------------")

for i in range(10):
    pass
# para tener hecho el codigo hasta que sepamos que va y no tire error



# for i in range(3, 7):
#     print(i)

print("------------------------")
# Desde cero hasta 10 de 2 en 2

# for i in range(0, 11, 2):
#     print(i)


# Ejemplo práctico: enviar emails (simulado)
usuarios = ["ana@mail.com", "bob@mail.com", "carlos@mail.com"]

for email in usuarios:
    print(f"Enviando bienvenida a {email}...")
    print(f"  ✓ Email enviado a {email}")

print(f"Proceso completado: {len(usuarios)} emails enviados")



print("+" + "-" * 36 + "+")
# Tabla de multiplicar
numero = int(input("¿De qué número quieres la tabla? "))

print(f"=== TABLA DEL {numero} ===")
# Usa un bucle for para mostrar la tabla...

for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")
##control + k y sin soltar control hacemos c, comenta multiples lineas
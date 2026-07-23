
# Realiza lo que se te pide usando las herramientas de Python
# Puedes copiar cada ejercicio en cada celda de tu notebook o bien
# Descargar este archivo y reemplazar las X por lo que debe ser


#E1: Guarda la variable en una cadena y con 4 decimales sin redondear
# el resultado debe ser '3.1416'
pi = 3.141592653589793
texto_pi = f"{pi:XXX}"
print(texto_pi)


print("ejercicio n 2")
#E2: Guarda la variable en una cadena  con 3 a la izquierda
# el resultado debe ser '00010'
entero = 10
entero_con_ceros = f"{entero:XXX}"
print(entero_con_ceros)


print("--- ejercicio n 3 ---")
#E3: Guarda la variable en una cadena  y en formato exponencial
# el resultado debe ser '1.000000e+04'
numerote = 10_000
numero_form_exp  = f"{numerote:XXX}"
print(numero_form_exp)



#E4: Guarda la variable en una cadena  y en formato exponencial
# el resultado debe ser '1e+04'
diez_mil = 10_000
diez_mil_exp  = f"{diez_mil:XXX}"
print(diez_mil_exp)



print("--- ejercicio num 5 ---")
# #E5: Rellena las XXX para crear la siguiente tabla
# 
# Tabla del 5 en gatites:
# ```python
# 
# 5 gatites x 2 = 10 gatites
# 5 gatites x 3 = 15 gatites
# 5 gatites x 4 = 20 gatites
# 5 gatites x 5 = 25 gatites
# 5 gatites x 6 = 30 gatites
# 5 gatites x 7 = 35 gatites
# 5 gatites x 8 = 40 gatites
# 5 gatites x 9 = 45 gatites
# 5 gatites x 10 = 50 gatites
# ```



numero = 5
tabla = f"Tabla del {XXX} en gatites:\n"
for i in range(2, 11):
    tabla += f"{XXX} gatites x {XXX} = {XXX * XXX} gatites\n"

print(tabla)



#E6: Rellena las XXX para alinear
#la tabla con el signo =
numero = 5
tabla_alineada = f"Tabla de {numero} en gatites:\n"
for i in range(2, 11):
    tabla_alineada += f"{numero} gatites x {i:XXX} = {numero * i} gatites\n"
    
print(tabla_alineada)




print("--- ejercicio num 7 ---")
#E7: Rellena las XXX para obtener el siguiente ouput:
#El total de 3 manzanas y 5 plátanos es $13.50.
p1 = "manzanas"
precio_1 = 2.5
cantidad_1 = 3

p2 = "plátanos"
precio_2 = 1.2
cantidad_2 = 5

total = precio_1 * cantidad_1 + precio_2 * cantidad_2
resumen = f"El total de {XXX} {XXX} y {XXX} {XXX} es ${total:XXX}."

print(resumen)  # Output: El total de 3 manzanas y 5 plátanos es $13.50.






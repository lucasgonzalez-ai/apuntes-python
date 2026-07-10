# La sintaxis generica es colocar un punto luego de la variable para llamar al metodo
# Escribiendo su nombre y cerrando entre parentesis

#Actividad
#Crea una lista con los numeros del 1 al 5.
#Agregar el número 6 al final de la lista.
#Insertar el número 0 al inicio de la lista.
#Eliminar el número 3 de la lista.
#Verificar si el numero 4 está en la lista
#Mostrar la lista final por pantalla

nums = [1, 2, 3, 4, 5]
print(nums)

nums.append(6)
print(nums)

nums.insert(0, 0)
print(nums)

nums.remove(3)
print(nums)

if 4 in nums:
    print("El numero 4 se encuentra en la lista")

print("La lista final es", nums)





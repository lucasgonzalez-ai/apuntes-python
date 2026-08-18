#keys(), values(), items(), update() y copy() — los métodos que más usarás.

cliente = {
    "nombre": "Carlos López",
    "email": "carlos@empresa.com",
    "plan": "premium",
    "gasto_mensual": 450.00,
}

# Obtener todas las claves y valores
print(list(cliente.keys()))    # ["nombre", "email", "plan", "gasto_mensual"]
print(list(cliente.values()))  # ["Carlos López", "carlos@empresa.com", ...]

# Iterar sobre clave-valor (muy común en datos)
for campo, valor in cliente.items():
    print(f"  {campo}: {valor}")

# Actualizar múltiples campos de golpe
cliente.update({"plan": "enterprise", "gasto_mensual": 890.00})

# Eliminar una clave
del cliente["email"]

# Copiar (cuidado: = NO copia, crea una referencia)
cliente_copia = cliente.copy()


'''
- .keys() → devuelve todas las claves del diccionario. list() las convierte en lista normal.
- .values() → devuelve todos los valores.
- .items() → devuelve pares (clave, valor) — perfecto para iterar con "for campo, valor in dict.items()".
- .update({...}) → actualiza/añade múltiples campos de golpe. Las claves existentes se sobreescriben.
- del cliente["email"] → elimina una clave. KeyError si no existe.
- .copy() → crea una copia SUPERFICIAL independiente.

Cuidado con la asignación: copia = original hace que ambos apunten al MISMO diccionario. Modificar uno modifica el otro. 
Usa .copy() para independencia.
'''
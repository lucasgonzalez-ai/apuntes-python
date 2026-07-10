# ¿Qué hace `enumerate()` exactamente?

La función `enumerate()` agrega un contador automático mientras recorremos una colección (lista, tupla, cadena, etc.).

Sin `enumerate()` solamente obtenemos el valor de cada elemento.

## Ejemplo sin `enumerate()`

```python
frecuencia_paciente_A = [77, 82, 75, 80, 79, 78]

for frecuencia in frecuencia_paciente_A:
    print(frecuencia)
```

### Salida

```text
77
82
75
80
79
78
```

En este caso conocemos cada valor, pero **no sabemos en qué posición de la lista se encuentra**.

---

## Ejemplo con `enumerate()`

```python
frecuencia_paciente_A = [77, 82, 75, 80, 79, 78]

for i, frecuencia in enumerate(frecuencia_paciente_A):
    print(i, frecuencia)
```

### Salida

```text
0 77
1 82
2 75
3 80
4 79
5 78
```

Ahora Python devuelve **dos valores en cada iteración**:

- `i`: el índice (posición) del elemento.
- `frecuencia`: el valor almacenado en esa posición.

---

# ¿Cómo funciona `enumerate()`?

Podemos imaginar que `enumerate()` forma pares de datos.

| Índice (`i`) | Valor (`frecuencia`) |
|--------------|----------------------|
| 0 | 77 |
| 1 | 82 |
| 2 | 75 |
| 3 | 80 |
| 4 | 79 |
| 5 | 78 |

Cada vez que el `for` realiza una iteración, desempaqueta uno de esos pares.

Primera iteración:

```python
i = 0
frecuencia = 77
```

Segunda iteración:

```python
i = 1
frecuencia = 82
```

Tercera iteración:

```python
i = 2
frecuencia = 75
```

Cuarta iteración:

```python
i = 3
frecuencia = 80
```

Quinta iteración:

```python
i = 4
frecuencia = 79
```

Sexta iteración:

```python
i = 5
frecuencia = 78
```

Cuando ya no quedan elementos en la lista, el ciclo `for` finaliza automáticamente.

---

# Prueba de escritorio

Supongamos el siguiente código:

```python
frecuencia_paciente_A = [77, 82, 75, 80, 79, 78]

for i, frecuencia in enumerate(frecuencia_paciente_A):
    print(i, frecuencia)
```

La ejecución ocurre de la siguiente manera:

| Iteración | `i` | `frecuencia` | Acción |
|-----------:|----:|-------------:|--------|
| 1 | 0 | 77 | Imprime `0 77` |
| 2 | 1 | 82 | Imprime `1 82` |
| 3 | 2 | 75 | Imprime `2 75` |
| 4 | 3 | 80 | Imprime `3 80` |
| 5 | 4 | 79 | Imprime `4 79` |
| 6 | 5 | 78 | Imprime `5 78` |

Salida final:

```text
0 77
1 82
2 75
3 80
4 79
5 78
```

---

# ¿Por qué `enumerate()` es útil?

Muchas veces no alcanza con conocer el valor de un elemento. También necesitamos saber **en qué posición aparece**.

Algunos ejemplos:

- Detectar en qué fila de un conjunto de datos existe un error.
- Encontrar la posición de un dato faltante (`None` o `NaN`).
- Mostrar el número de registro donde ocurre una anomalía.
- Identificar el instante en que una serie temporal supera un determinado umbral.
- Enumerar elementos para mostrarlos al usuario.

En el siguiente ejemplo:

```python
for i, frecuencia in enumerate(frecuencia_paciente_A):
    if frecuencia > 80:
        print(f"¡Alerta en el registro {i}! Valor: {frecuencia}")
```

No solamente sabemos que existe una frecuencia cardíaca elevada, sino también **en qué registro fue detectada**, facilitando su localización para un análisis posterior.

---

# ¿Qué devuelve realmente `enumerate()`?

Conceptualmente, `enumerate()` genera una secuencia de pares `(índice, valor)`.

Es decir, para la lista:

```python
[77, 82, 75, 80]
```

Podemos imaginar que produce algo similar a:

```text
(0, 77)
(1, 82)
(2, 75)
(3, 80)
```

Luego el ciclo `for` desempaqueta automáticamente cada par en dos variables:

```python
for i, frecuencia in enumerate(frecuencia_paciente_A):
```

equivale a decir:

- guardar el índice en `i`
- guardar el valor en `frecuencia`

---

# Resumen

`enumerate()` permite recorrer una colección obteniendo simultáneamente:

- la posición del elemento (índice),
- el valor almacenado en esa posición.

Su sintaxis es:

```python
for indice, valor in enumerate(coleccion):
    ...
```

Es una función muy utilizada en Python porque evita tener que llevar un contador manual y hace que el código sea más claro, legible y fácil de mantener.
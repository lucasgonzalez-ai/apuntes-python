#!/usr/bin/env python
# coding: utf-8

# In[1]:


## E1
## Sin usar paquetes instalados, crea una nueva lista
## con el formato YYYY-MM-DD  y que se vea, por ejemplo:
## '2023-Jan-01' en lugar de "202301Jan"
## Tip puedes usar list comprehension y sumas de string
## Guarda las fechas con el nuevo formato en fechas_formateadas
## Cuida los espacios, debe tener el formato identico al mostrado.
fechas = ["202301Jan", 
          "202302Feb", 
          "202303Mar", 
          "202304Apr", 
          "202305May", 
          "202306Jun", 
          "202307Jul",
          "202308Aug", 
          "202309Sep", 
          "202310Oct"]

fechas_formateadas = []

for fecha in fechas:
    #Extraemos cada parte usando 'slicing' [inicio:fin]
    anio = fecha[0:4]  # Toma los caracteres desde el índice 0 hasta el 3 ('2023')
    dia = fecha[4:6]   # Toma los caracteres desde el índice 4 hasta el 5 ('01')
    mes = fecha[6:9]   # Toma los caracteres desde el índice 6 hasta el 8 ('Jan')
    
    #Sumamos (concatenamos) los strings agregando los guiones en el orden pedido
    nueva_fecha = anio + "-" + mes + "-" + dia
    
    #Agregamos la nueva fecha ya formateada a nuestra lista final
    fechas_formateadas.append(nueva_fecha)

print(fechas_formateadas)


# your code here


# In[ ]:





# In[4]:


## E2
## Sin usar paquetes instalados, genere una nueva lista
## con el formato YYYY-MM-DD reemplazando Marzo por el
## número del mes correspondiente, es decir transforma
## "Marzo 10, 2023" a '2023-03-10'
## Tip puedes usar list comprehension y .replace
## Guarda las fechas con el nuevo formato en fechas_es_formateadas
## Cuida los espacios, debe tener el formato identico al mostrado.

fechas_es = [
    "Marzo 10, 2023",
    "Marzo 11, 2023",
    "Marzo 12, 2023",
    "Marzo 13, 2023",
    "Marzo 14, 2023",
    "Marzo 15, 2023",
    "Marzo 16, 2023",
    "Marzo 17, 2023",
    "Marzo 18, 2023",
    "Marzo 19, 2023",
]

fechas_es_formateadas = []

for fecha in fechas_es:
    
    #Reemplazamos 'Marzo' por su número correspondiente '03'
    texto_mes = fecha.replace("Marzo", "03")       # Queda: "03 10, 2023"
    
    #Quitamos la coma sobrante reemplazándola por un texto vacío ""
    texto_limpio = texto_mes.replace(",", "")       # Queda: "03 10 2023"
    
    # 5. Separamos el texto usando los espacios como divisor
    partes = texto_limpio.split(" ")                # Queda la lista: ['03', '10', '2023']
    
    # 6. Extraemos cada componente por su posición en la lista 'partes'
    mes = partes[0]
    dia = partes[1]
    anio = partes[2]
    
    # 7. Reordenamos con el formato YYYY-MM-DD usando un f-string
    nueva_fecha = f"{anio}-{mes}-{dia}"
    
    # 8. Agregamos el resultado a la lista final
    fechas_es_formateadas.append(nueva_fecha)
 


print(fechas_es_formateadas)
# your code here


print("+" + "-" * 36 + "+")
## E3
## Sin usar paquetes instalados, genere una nueva lista
## con el formato YYYY-MM-DD reemplazando Marzo por el
## número del mes correspondiente, es decir transforma
## "Marzo 10, 2023" a '2023-03-10'
## Tip puedes usar list comprehension, replace o  un diccionario para hacer el replace
## Guarda las fechas con el nuevo formato en meses_formateados
## Cuida los espacios, debe tener el formato identico al mostrado.

fechas = [
    "Marzo,30,2023",
    "Marzo,31,2023",
    "Abril,29,2023",
    "Abril,30,2023",
    "Mayo,1,2023",
    "Mayo,2,2023",
    "Mayo,8,2023",
    "Mayo,9,2023"
]


diccionario_meses = {
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05"
}

meses_formateados = []

for fecha in fechas:
    
    #Separamos el texto usando la coma como divisor
    partes = fecha.split(",")          # Ej: "Mayo,1,2023" se convierte en ['Mayo', '1', '2023']
    
    #Extraemos cada componente de la lista resultante
    mes_texto = partes[0]              # 'Mayo'
    dia = partes[1]                    # '1'
    anio = partes[2]                   # '2023'
    
    #Traducimos el mes de texto a número usando nuestro diccionario
    mes_numero = diccionario_meses[mes_texto]  # Busca 'Mayo' en el diccionario y devuelve '05'
    
    #Aseguramos que el día tenga 2 dígitos rellenando con ceros a la izquierda
    dia_formateado = dia.zfill(2)      # '1' pasa a ser '01', pero '30' se queda como '30'
    
    #Unimos todo con el formato YYYY-MM-DD
    nueva_fecha = f"{anio}-{mes_numero}-{dia_formateado}"
    
    #Agregamos el resultado a la lista
    meses_formateados.append(nueva_fecha)


print(meses_formateados)

# your code here


print("+" + "-" * 36 + "+")
## E4 
## Limpia el texto para que te quedes con una lista que contenga elementos con la fecha y hora.
## La hora debe ser formato PM y debe usar guión medio, debe verse como:
## '09-03-2022 07:03:36 PM'
## en formato 'dd-mm-yyyy HH:MM:SS PM'
## con un espacio entre elementos.
## Cuida los espacios, debe tener el formato identico al mostrado, 
## toma como referencia las comillas.
## La secuencia sugerida es:
## 1. Divide el texto en elementos de una lista
## 2. Elimina los elementos vacios vacios de la lista
## 3. Divide cada renglón que ya tienes como un elemento en sub elementos
## 4. Guarda en una nueva lista solo el elemento que contiene las fechas
## 5. Dale el formato pedido reemplazando los caracteres adecuados.


texto = '''
Q,+001.61,-001.51,-000.16,M,00,2D,1,09/03/2022 07:03:36 p. m.
Q,+000.57,-001.01,-000.44,M,00,2B,2,09/03/2022 07:03:37 p. m.
Q,+000.06,-000.93,+000.51,M,00,27,3,09/03/2022 07:03:38 p. m.
Q,+001.51,-000.76,-000.31,M,00,2F,4,09/03/2022 07:03:39 p. m.
Q,+002.12,-001.34,-000.62,M,00,2A,5,09/03/2022 07:03:40 p. m.
Q,+000.81,-000.61,+000.35,M,00,27,6,09/03/2022 07:03:41 p. m.
Q,+000.48,-000.43,-000.02,M,00,20,7,09/03/2022 07:03:42 p. m.
Q,+000.32,-000.62,+000.11,M,00,2A,8,09/03/2022 07:03:43 p. m.
Q,+001.38,-001.14,+000.48,M,00,2D,9,09/03/2022 07:03:44 p. m.
'''

# 1. Divide el texto en elementos de una lista (separando por salto de línea)
lineas = texto.split("\n")

# Lista final donde guardaremos los resultados
fechas_pm = []

# 2. Empezamos a iterar y eliminamos los elementos vacíos
for linea in lineas:
    
    # Verificamos que la línea no esté vacía antes de procesarla
    if linea != "":
        
        # 3. Divide cada renglón en sub elementos usando la coma
        elementos = linea.split(",")
        
        # 4. Guarda solo el elemento que contiene las fechas (el último)
        # En Python, el índice -1 siempre representa el último elemento de la lista
        fecha_cruda = elementos[-1]
        
        # 5. Dale el formato pedido reemplazando los caracteres
        # Primero cambiamos las barras por guiones medios
        fecha_con_guiones = fecha_cruda.replace("/", "-")
        
        # Luego cambiamos 'p. m.' por 'PM'
        fecha_final = fecha_con_guiones.replace("p. m.", "PM")
        
        # Agregamos a nuestra lista
        fechas_pm.append(fecha_final)

# Comprobamos el resultado
print(fechas_pm)





## E5
## En el siguiente conjunto de datos, te han dado 10 mediciones
## conserva el orden de los números, pero pon como primer elemento
## la fecha usando el elemento 1,4 y 6 de cada sublista, que son
## mes, año y día. El formato de fecha debe ser YYYY-MM-DD
## La primer sublista debe verse como
## ['2023-Enero-1', 18.2, 345, 938, 75.6, 425, 624]
## Nota como se conserva el orden de los datos y las columnas 1,4 y 6 
## han formado la fecha y es ahora el primer dato
## y que los numeros no tienen entrecomillado, por lo cual son enteros 
## los que no tienen decimal y flotantes los que tienen decimal.
## guarda en la variable datos_fecha
## Cuida los espacios, debe tener el formato identico al mostrado.
datos = [
    ['18.2', 'Enero', '345', '938', '2023', '75.6', '1', '425', '624'],
    ['73.9', 'Febrero', '856', '432', '2023', '29.5', '2', '781', '952'],
    ['87.3', 'Marzo', '465', '398', '2023', '72.9', '3', '612', '432'],
    ['38.1', 'Abril', '293', '582', '2023', '72.9', '4', '153', '867'],
    ['97.3', 'Mayo', '159', '246', '2023', '82.3', '5', '746', '598'],
    ['29.4', 'Junio', '867', '598', '2023', '13.5', '6', '628', '392'],
    ['73.9', 'Julio', '236', '985', '2023', '73.8', '7', '195', '382'],
    ['95.7', 'Agosto', '834', '582', '2023', '62.5', '8', '748', '953'],
    ['23.4', 'Septiembre', '865', '392', '2023', '58.7', '9', '341', '782'],
    ['78.3', 'Octubre', '528', '974', '2023', '23.7', '10', '654', '392']
]

datos_fecha = []

# your code here

# 1. Preparamos la lista final vacía
datos_fecha = []

# 2. Iteramos sobre cada sublista (fila) dentro de nuestros datos
for fila in datos:
    
    # 3. Extraemos las partes de la fecha usando sus índices (1, 4 y 6)
    mes = fila[1]
    anio = fila[4]
    dia = fila[6]
    
    # 4. Armamos la fecha tal como pide el ejemplo de la instrucción
    fecha = f"{anio}-{mes}-{dia}"
    
    # 5. Creamos una nueva sublista que arranque con esta fecha que acabamos de armar
    nueva_fila = [fecha]
    
    # 6. Agrupamos los índices de los números que nos quedaron (saltando el 1, 4 y 6)
    indices_numeros = [0, 2, 3, 5, 7, 8]
    
    # 7. Iteramos sobre estos índices para extraer y convertir cada número
    for i in indices_numeros:
        valor_texto = fila[i]
        
        # 8. Evaluamos si es entero o flotante buscando el punto decimal
        if "." in valor_texto:
            # Si tiene un punto, lo convertimos a float (decimal) y lo agregamos
            nueva_fila.append(float(valor_texto))
        else:
            # Si no tiene punto, lo convertimos a int (entero) y lo agregamos
            nueva_fila.append(int(valor_texto))
            
    # 9. Finalmente, agregamos esta fila ya procesada a nuestra lista principal
    datos_fecha.append(nueva_fila)

# Comprobamos el resultado imprimiendo la primera fila para comparar con la consigna
print(datos_fecha[0])



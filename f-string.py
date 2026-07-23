# Las variables permiten almacenar datos, y las f-strings ayudan a presentar o formatear esos datos de manera legible o conveniente 

nombre = "Vicente"
edad = 32
visual = "Looker Studio"

print(f"Mi amigo {nombre} tiene {edad} anios y utiliza {visual} para visualizar Datos")

databases = "My SQL"
database2 = "PostgreSQL"

libreria1 = "Pandas"
libreria2 = "Numpy"
libreria3 =  "Matplotlib"


print(f"Las bases de datos mas utilizadas son {databases} y {database2} y las librerias mas utilizadas en Data Science son {libreria1} {libreria2} y {libreria3}")

print("--- --- --- --- ---")

c = 106
f = 9/5*c +32

print(f"{c} grados centigrados equivale a {f} grados farenheit")

# Si quisiera darle formato sin decimale o con 3 decimales podria hacer
print("--- Sin --- decimales ---")
print(f"{c} grados centigrados equivale a {f:.0f} grados farenheit")

print("--- Con --- decimales ---")
print(f"{c} grados centigrados equivale a {f:.3f} grados farenheit")
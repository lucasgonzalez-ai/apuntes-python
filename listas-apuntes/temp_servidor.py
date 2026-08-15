# Temperaturas del servidor (lecturas cada 2 horas)
temperaturas = [62.3, 65.1, 71.8, 68.4, 76.2, 73.9, 69.5, 64.8, 61.2, 67.7, 72.1, 70.3]
UMBRAL_CRITICO = 75.0

maxima = max(temperaturas)              # <- # <- la lectura más alta
minima = min(temperaturas)                 # <- la lectura más baja
promedio = sum(temperaturas) / len(temperaturas)          # <- suma / cuántas lecturas hay
supero_umbral = True                    # <- ¿la máxima supera el umbral?

# Reporte
print("MONITOREO TÉRMICO DEL SERVIDOR")
print(f"Máxima: {maxima:.1f}°C")
print(f"Mínima: {minima:.1f}°C")
print(f"Promedio: {promedio:.1f}°C")
print(f"¿Alerta térmica? {supero_umbral}")

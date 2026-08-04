# Simulador de ahorro mensual
objetivo = float(input("¿Cuánto necesitas ahorrar? ($): "))
ahorro_mensual = float(input("¿Cuánto puedes ahorrar al mes? ($): "))

ahorrado = 0.0
meses = 0

print(f"")
print(f"=== PLAN DE AHORRO ===")
print(f"Objetivo: {objetivo:.2f}$")
print(f"Ahorro mensual: {ahorro_mensual:.2f}$")
print(f"")

while ahorrado < objetivo:
    meses = meses + 1
    ahorrado = ahorrado + ahorro_mensual
    porcentaje = (ahorrado / objetivo) * 100
    if porcentaje > 100:
        porcentaje = 100
    barra = "█" * int(porcentaje / 5) + "░" * (20 - int(porcentaje / 5))
    print(f"Mes {meses:2d}: {ahorrado:8.2f}$ [{barra}] {porcentaje:.0f}%")

print(f"")
print(f"🎉 ¡Objetivo alcanzado en {meses} meses!")
if meses <= 6:
    print("¡Rápido! Menos de medio año.")
elif meses <= 12:
    print("Un año. Paciencia y constancia.")
else:
    print(f"Son {meses // 12} años y {meses % 12} meses. ¡Ánimo!")